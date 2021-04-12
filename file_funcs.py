from striprtf.striprtf import rtf_to_text
import docx2txt

r = re.compile(r'\w+')

punctuation_strip = str.maketrans('', '', string.punctuation)

