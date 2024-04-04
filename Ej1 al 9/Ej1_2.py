text = """ NumPy is a community-driven open source project developed by a diverse group of contributors. The NumPy leadership has made a strong commitment to creating an open, inclusive, and positive community. Please read the NumPy Code of Conduct for guidance on how to interact with others in a way that makes our community thrive.

Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
help us stay on top of new and old issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
For more information about the ways you can contribute to NumPy, visit our website. If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invitation).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.
"""

special_characters = ('.', ',', '@', '-', '(', ')', '!')
for character in special_characters:
        if (character in text):
            text = text.replace (character, '')

lines = []
lines = text.split('\n')

vocals = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')

for line in lines:
    words = line.split(' ') 
    if len(words) > 1 and words[1][0] in vocals:
        print (line)

from collections import Counter
word_4 = text.split(' ')

word_4 = [word for word in word_4 if len(word) >= 4]

counter_word = Counter(word_4)

print (f'Palabra de mas de 4 caracteres que mas aparece: ', counter_word.most_common(1)[0][0])
