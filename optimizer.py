import argparse

from openai import OpenAI
import os

def main():
    parser = argparse.ArgumentParser(description='Optimize resume for a certain job description')
    parser.add_argument('--resume', '-r', help='Path to input resume file(markdown format)')
    parser.add_argument('--description', '-d', help='Path to the job description')
    parser.add_argument('--output', '-o', help='Path to output file')

    args = parser.parse_args()

    # Check if API key is set
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it by running: set OPENAI_API_KEY=your_api_key_here")
        exit(1)

    client = OpenAI(api_key=api_key)

    input_resume = args.resume
    input_description = args.description
    output_path = args.output

    with open(input_resume, "r", encoding='utf-8') as f:
        md_resume = f.read()

    with open(input_description, "r", encoding='utf-8') as f:
        job_description = f.read()

    prompt=f"""
            I will provide you with a resume(in markdown format) and a job description.\
            Your task is to:\
            Analyze the job description to identify key skills, qualifications, and responsibilities the employer values most.
            Adapt my resume to emphasize the most relevant experience, skills, and achievements.
            Use clear, professional, and concise language.
            Highlight accomplishments with measurable results (where possible).
            Reorder or rephrase bullet points to better align with the role and to emphasize relevant skills and achievements.
            Adjust section emphasis (e.g., skills, projects, experience) to match what the job stresses.
            Ensure the updated resume remains truthful, polished, and ATS-friendly while maintaining Markdown formatting.
        
            ### Here is my resume in Markdown:
            {md_resume}

            ### Here is the job description:
            {job_description}

            Return the updated resume in Markdown format.
            Also don't use emojis and don't give me other text after or before. Just the resume.
            """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
            ]
        )
    
        resume = response.choices[0].message.content

        with open(output_path, "w", encoding='utf-8') as f:
            f.write(resume)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()