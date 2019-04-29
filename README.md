# SpamFiltration
Spam Filtration or Classification of E-Mails using Naive Bayes.

# Abstract
Email spam is operations which are sending the undesirable messages to different email client. E-Mail spam is the very recent problem for every individual. The E-Mail spam is nothing, it's just an advertisement of any company/product or any kind of virus receiving by the email client mailbox without any notification. To solve this problem the different spam filtering techniques are used. Here we are using real-time data set for classification of spam and non-spam emails. The result is to increase the Accuracy of the system.

# Working
The Data set used is Enron E-Mail Data Set, in these project it contains about <b>(2000)</b> E-Mail Data set.<br><br>
The File <br><b>spam.py</b>, it uses <b>Naive bayesian</b> Classification creates Dictionary of all Repeated words and generates a Model which is "<b>text-classification.mdl</b>" File.
<br><br>
The File <br><b>detector.py</b>, it uses the generated <b>text-classification.mdl</b>, file for testing purpose, so as to classify whether the input email is <b>Spam</b> or <b>Ham</b>
<br><br>
To Download <b><a href="http://www.cs.cmu.edu/~enron" target="_blank">Enron Email Data set</a></b> Click here.

# Commands
<li><b>$ python spam.py</b> &nbsp;&nbsp;&nbsp;, then execute</li>
<li><b>$ python detector.py</b></li>