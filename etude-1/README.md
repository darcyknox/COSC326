Author: Darcy Knox
COSC326 S1 2020
Etude 1
Email Addresses

Written in Python 3.7.6

To input from a file, use the command:
python3 etude-1.py < filename.txt

To input from the command line, use the command:
python3 etude-1.py


Valid test cases (expected) used:

a.b_c-d@domain.com
first_last@domain.co.nz
firstlast_at_domain_dot_com
CEO@InsuroCorp.com
gerry_at_research.techies_dot_co.uk
cath@[139.80.91.50]
b_at_g_dot_com
brad@dom.co.uk
first.last@dom.com
mail1.2@dom.com
mail-mail@[12.12.12.12]
mail.mail@dom.co.co.co.nz
mail@dom.co.uk.co.nz.co.ca
mail@dom.co.nz
mail@cs.co.uk
mail@dom.co.uk
mail_mail@dom.com
at_at_at_at_dot_com


Invalid test cases (expected) used:

first_last@dom.com.nz
maffu@cs.otago.ac.nz
bob.mail.com
mail@dom..com
n-@dom.com
mail.co.nz
mail@dom1..dom2.com
n@a@m@e@dom.co.nz
.mail@dom.com
mail@dom..com
 -mail@dom.com
mail@dom_dot__dot_com
mail@dom_dot_.com
#@%^%#$@#$@#.com
mail.co.nz
@dom.com
mail@mail@dom.com
mail@dom
mail@dom.
mail@-example.com
mailonly
mail@dom.com_
mail_@l.com
mail#mail@dom.com
mail__mail@dom.com
mail-_mail@dom.com
mail-mail@dom.com_
mail@dom.[12.12.12.12]
mail@[123.12.12.12].com
mail@[123.12.12.12.12]
mail[123.12.12.12]
@[123.12.12.12]
mail@[12.12.12.12][23.23.23.23]
mail.dom.com
mail.._at_dom.com
mail.-mail@dom.com
mail.dom@
mail.mail@dom-dom.com
ma+il@dom.com
mail @dom.com
mail@dom.com.
mail@.dom.com
mail@domdotcom


Resources used:

regex101.com
www.regular-expressions.info
