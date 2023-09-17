import openpyxl


class ExcelInput:
    def create_excel_file(self, links, output_filename):
        # Create a new Excel workbook
        workbook = openpyxl.Workbook()

        # Select the active sheet (first sheet)
        sheet = workbook.active

        # Set the header for the first column
        sheet['A1'] = 'Links'

        # Add links to the spreadsheet one by one
        for i, link in enumerate(links, start=2):  # Start from the second row
            sheet[f'A{i}'] = link

        # Save the workbook to the specified output filename
        workbook.save(output_filename)