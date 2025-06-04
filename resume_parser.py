import pymupdf


def extract_text_pdf(file_path):
    all_text=""
    doc = pymupdf.open(file_path)
    for page in doc:  # iterate through the pages
      page_text = page.get_text() #gets the text from the pgs in form of string 
      all_text += page_text # the string gets added with the new text from each page untill we allitrate thrpught all the pages
    return all_text
