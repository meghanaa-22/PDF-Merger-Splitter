from pypdf import PdfReader, PdfWriter, PdfMerger
import os


def merge_pdfs():
    try:
        n = int(input("Enter number of PDF files to merge: "))

        merger = PdfMerger()

        for i in range(n):
            pdf_file = input(f"Enter PDF file {i+1} name: ")

            if os.path.exists(pdf_file):
                merger.append(pdf_file)
            else:
                print(f"{pdf_file} not found!")

        output_file = input("Enter output merged PDF name: ")

        with open(output_file, "wb") as file:
            merger.write(file)

        merger.close()

        print(f"\nPDFs merged successfully into '{output_file}'")

    except Exception as e:
        print("Error:", e)


def split_pdf():
    try:
        pdf_file = input("Enter PDF file name to split: ")

        if not os.path.exists(pdf_file):
            print("File not found!")
            return

        reader = PdfReader(pdf_file)

        total_pages = len(reader.pages)

        print(f"\nTotal Pages: {total_pages}")

        output_folder = "Split_PDFs"

        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        for page_num in range(total_pages):

            writer = PdfWriter()

            writer.add_page(reader.pages[page_num])

            output_path = os.path.join(
                output_folder,
                f"Page_{page_num + 1}.pdf"
            )

            with open(output_path, "wb") as file:
                writer.write(file)

        print(f"\nPDF split successfully.")
        print(f"Files saved in '{output_folder}' folder.")

    except Exception as e:
        print("Error:", e)


def pdf_info():
    try:
        pdf_file = input("Enter PDF file name: ")

        if not os.path.exists(pdf_file):
            print("File not found!")
            return

        reader = PdfReader(pdf_file)

        print("\n----- PDF DETAILS -----")
        print("Total Pages:", len(reader.pages))

    except Exception as e:
        print("Error:", e)


while True:

    print("\n========== PDF TOOL ==========")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. PDF Information")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        merge_pdfs()

    elif choice == "2":
        split_pdf()

    elif choice == "3":
        pdf_info()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")