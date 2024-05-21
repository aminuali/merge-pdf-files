"""
Created on Fri May 17 15:04:56 2024

@author: NITRON 5
"""
import streamlit as st
import pypdf
from io import BytesIO

def merge_pdfs(input_pdfs, output_pdf):
    """
    Function to merge PDFs
    """
    pdf_merger = pypdf.PdfMerger()

    for pdf_file in input_pdfs:
        pdf_merger.append(pdf_file)

    with open(output_pdf, 'wb') as output:
        pdf_merger.write(output)

def main():
    """
    Streamlit app for PDF merging
    """
    st.title("PDF Merger")
    st.write("Upload your PDF files and merge them into a single document.")

    uploaded_files = st.file_uploader("Select PDFs to Merge", type="pdf", accept_multiple_files=True)

    output_filename = st.text_input("Output Filename:", "merged.pdf")

    if st.button("Merge PDFs"):
        if uploaded_files:
            input_files = [BytesIO(file.getvalue()) for file in uploaded_files]
            merge_pdfs(input_files, output_filename)
            st.success(f"PDF files merged successfully! Download '{output_filename}'.")
            
            # Provide a download link for the merged PDF
            with open(output_filename, 'rb') as file:
                st.download_button(label="Download Merged PDF", data=file, file_name=output_filename, mime="application/pdf")
        else:
            st.error("Please select some PDF files to merge.")

if __name__ == "__main__":
    main()
