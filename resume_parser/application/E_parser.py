from parserr import resume_to_structured
import json
from JD_parser import resume_to_structured as res
OPENAI_API_KEY = "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"
parser = resume_to_structured(OPENAI_API_KEY)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(parser.ending_process("Luis's Resume.pdf")))
    
J_parser = res(OPENAI_API_KEY)
re = ""
with open('borneo-JD.txt', 'r') as f:
    for line in f.readlines():
        re = re + line
# f = open('borneo-JD.txt', 'r')
with open("sampl.json", "w") as outfile:
    outfile.write(json.dumps(J_parser.ending_process(JD = re)))