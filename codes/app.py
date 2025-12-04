import streamlit as st
import json
from jd_pdf_parser import parse_job_description_pdf
from google_finder import find_candidates_for_jd
from resume_parser import parse_resume_file
from matching import compute_match_for_resume
from linkedin_finder import find_linkedin_candidates


# ============================================================
# PAGE SETUP
# ============================================================
st.set_page_config(
    page_title="AI Hiring Platform",
    layout="wide",
)


st.title("🤖 AI Hiring Platform — JD Analyzer + Resume Finder + LinkedIn Finder")


# ============================================================
# SECTION 1 — JOB DESCRIPTION ANALYZER
# ============================================================
st.header("📄 1. Job Description Analyzer")

uploaded_jd = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_jd:
    # Save JD temporarily
    ext = uploaded_jd.name.split(".")[-1]
    jd_path = f"uploaded_jd.{ext}"

    with open(jd_path, "wb") as f:
        f.write(uploaded_jd.getbuffer())

    # Parse JD
    st.info("⏳ Extracting details from Job Description...")
    jd = parse_job_description_pdf(jd_path)
    st.success("JD processed successfully! 🎉")


    # ---------------- DISPLAY JD INFO ----------------
    st.subheader("📌 Extracted Skills")
    st.write(", ".join(jd["skills"]) if jd["skills"] else "No skills detected.")

    st.subheader("📌 Responsibilities")
    if jd["responsibilities"]:
        for r in jd["responsibilities"]:
            st.write("- " + r)
    else:
        st.write("No responsibilities detected.")

    st.subheader("📌 Seniority Level")
    st.write(jd["seniority_level"])

    st.subheader("📌 Domain")
    st.write(jd["domain"])

    st.subheader("📌 Location (auto-detected)")
    st.write(jd.get("location", "Not Specified"))

    st.subheader("📌 Tech Stack")
    st.write(", ".join(jd["tech_stack"]) if jd["tech_stack"] else "None")

    st.subheader("📌 Keywords")
    st.write(", ".join(jd["keywords"]) if jd["keywords"] else "None")

    st.markdown("---")



    # ============================================================
    # SECTION 2 — GOOGLE RESUME FINDER
    # ============================================================
    st.header("🔍 2. Google Resume Finder (Public PDF Resumes)")

    max_dl = st.slider("Max number of resumes to fetch", 1, 20, 8)
    show_text = st.checkbox("Show extracted resume text", False)

    if st.button("Search Public Resumes (Google)"):
        st.warning("🔍 Searching Google for resume PDFs... This may take 10–20 seconds...")

        # Wrap parser + scorer for google_finder
        def parse_and_score(path, jd_obj, source_url=None):
            resume_data = parse_resume_file(path)
            resume_data["path"] = path
            return compute_match_for_resume(resume_data, jd_obj, source_url)

        results = find_candidates_for_jd(
            jd,
            parse_and_score_fn=parse_and_score,
            max_downloads=max_dl
        )

        if not results:
            st.error("❌ No resumes found. Try increasing max downloads.")
        else:
            st.success(f"🎉 Found {len(results)} public resumes!")

            # Display results
            for i, r in enumerate(results, start=1):
                st.markdown(f"### {i}. **{r['candidate_name']}** — Score: **{r['final_score']:.3f}**")

                st.write("🔗 Source:", r["source_url"])
                st.write("**Matched Skills:**", ", ".join(r["matched_skills"]) or "None")
                st.write("**Missing Skills:**", ", ".join(r["missing_skills"]) or "None")

                st.write(f"Skill Score: **{r['skill_score']:.3f}**  |  "
                         f"Semantic Score: **{r['embed_score']:.3f}**  |  "
                         f"Responsibility Score: **{r['resp_score']:.3f}**")

                if show_text:
                    with st.expander("📄 View Resume Text"):
                        st.write(r["cleaned_text"])

                st.markdown("---")

            st.download_button(
                "📥 Download Results (JSON)",
                data=json.dumps(results, indent=2),
                file_name="google_resume_results.json"
            )

    st.markdown("---")



    # ============================================================
    # SECTION 3 — LINKEDIN CANDIDATE FINDER
    # ============================================================
    st.header("🔗 3. LinkedIn Candidate Finder (via Google Search — LEGAL)")

    st.write("""
    This tool finds **public LinkedIn profiles** using Google SERP (legal + safe),  
    extracts candidate skills from Google snippets,  
    and matches them against your Job Description.
    """)

    if st.button("Search LinkedIn Candidates"):
        st.info("🔎 Searching Google for LinkedIn profiles that match your JD...")

        linkedin_results = find_linkedin_candidates(jd)

        if not linkedin_results:
            st.error("❌ No LinkedIn candidates found.")
        else:
            st.success(f"🎉 Found {len(linkedin_results)} potential candidates from LinkedIn!")

            # Display LinkedIn results
            for i, c in enumerate(linkedin_results, start=1):
                st.markdown(f"### {i}. **{c['name']}** — Match Score: **{c['match_score']}%**")

                st.write("👤 Headline:", c["headline"])
                st.write("🛠 Skills Found:", ", ".join(c["skills"]))
                st.write("✔ Matched Skills:", ", ".join(c["matched_skills"]))
                st.write("❌ Missing Skills:", ", ".join(c["missing_skills"]))
                st.write("🔗 LinkedIn Profile:", c["url"])

                st.markdown("---")

            st.download_button(
                "📥 Download LinkedIn Candidate Results",
                data=json.dumps(linkedin_results, indent=2),
                file_name="linkedin_candidates.json"
            )
