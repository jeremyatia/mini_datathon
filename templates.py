from config import context_markdown, content_markdown, evaluation_content, data_instruction_commands

# The following templates are markdowns
overview = """
## Context
""" + context_markdown + \
"""
## Content
""" + content_markdown + \
"""
 <br />  <br />  <br />  <br />  <br />  <br />  <br />  <br />
Made with Love by [Jeremy Atia](https://il.linkedin.com/in/jatia/en) using [mini_datathon](https://towardsdatascience.com/mini-datathon-the-platform-you-need-for-your-data-science-hackathon-b386cd125ca2).
"""

data = """
In order to get the data simply run the following commands:
""" + data_instruction_commands + \
"""
Please submit your predictions in the exact same format as y_train.
"""

evaluation = evaluation_content
