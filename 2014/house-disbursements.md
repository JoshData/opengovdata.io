---
layout: default
permalink: /house-disbursements/
page_previous: /2014/the-later-memorandums/
page_next: /2014/state-laws-the-district-columbia-code/
title: "House Disbursements"
---
House Disbursements
===================

By Joshua Tauberer. April 2012.
{: .byline }


When the U.S. House of Representatives began publishing its disbursements (operational spending) records online in 2009, I evaluated the quality of the data release according to the principles of open government data discussed earlier. Disbursements include how much congressmen and their staffs are paid, what kinds of expenses they have, and who they are paying for those services. The disbursements release makes a great case study in how to do data transparency.

Uses of House Disbursement Records
----------------------------------

In evaluating the quality of the data, I looked to the subsequent uses of the data to understand its purpose. After all, it is impossible to evaluate data quality in the absence of a purpose. <span>Sunlight Foundation</span>’s Daniel Schuman has investigated a very serious question: “whether Congress has the support necessary to do its job.” Based on the disbursement data plus historical records, Schuman found that the number of congressional staff has decreased 13 percent since 1979, and in particular congressional committee staff, which do most of the policy work, has decreased 37 percent in the same time. Most Hill staff salaries have remained the same over the last two decades (accounting for inflation), and with equivalent private sector jobs often paying more it is no surprise that Congressional staff will often leave for private sector jobs. This paves the way of the revolving door, in which former staff make use of their contacts to advance the agenda of their new employer.[^1] In a later analysis from the Sunlight Foundation, Lee Drutman compared the disbursement data with registered lobbyist data to approximate the magnitude of this revolving door[^2] and the effect on staff turnover[^3] Putting aside whether the revolving door may be inappropriate or illegal, it indicates a clear problem of unequal access to policy-making.

I had run several statistical regression analyses on the disbursement data and found that offices spent more on some staff positions for each year the congressman was in office — \$2,500 more on staff assistants each year — but not on others — such as legislative correspondents and chiefs of staff. This might mean that congressmen make sure they are on an equal footing by all hiring from the same pool of experienced candidates, and also that chiefs of staffs don’t consider it a perk (i.e. willing to take a pay cut) or a detriment (i.e. wanting more pay) to work for new or older congressmen either. Also reported in the dataset is the yearly expense on franked mail. This interestingly decreased by \$1,300 per year in office, suggesting that greener congressmen rely more on franked mail for public relations than more senior congressmen who might have access to other methods of public relations such as coverage in the press.[^4]

A third use of the data is by Legistorm.com, which is a database of congressional staff and salaries and is often used by lobbyists and other outsiders to locate potential points of contact within the Hill. Helping lobbyists was surely not an intended use of the data. The data was released for the purposes of disclosure and should be evaluated first on how well it lets the public root out inappropriate spending, second on how well it helps the public understand trends in spending, and third on unexpected uses such as Legistorm’s use of the data.

Evaluating the data release
---------------------------

The first thing the release did right was put the data online (currently at [disbursements.house.gov](http://disbursements.house.gov/)), free of charge. The downloads of current information and archived releases are clear links at semi-permanent locations. The data format (PDF) is an open non-proprietary standard, and the data is released in bulk because each release is provided as a single file download. The release is provided on a <span>non-discriminatory</span> basis (i.e. no registration requirement), and use is not restricted by any license terms or by law. Furthermore, the PDF files are digitally signed by the <span>Government Printing Office</span> which establishes their <span>provenance</span>. The data is also released on a relatively <span>timely</span> basis. The website indicates the statements are published within 60 days of the end of the quarter, and the most recent disclosure at the time of writing seems to have been published as quickly as 11 days after the end of the previous quarter. There were also no technological choices that could be construed as an endorsement.

One of the more exemplary aspects of the data release was its <span>documentation</span>, which included an explanation of the reporting process, a FAQ, a glossary, and a table of transaction codes found in the document, all crucial for anyone reading or analyzing the information. This was one of the best examples of documentation I’ve seen for government data of this kind.

The data release comprises information that is as dis-aggregate as is reasonably possible (i.e. it is primary). The disclosure comprises essentially quarterly totals of line items. Because the documentation actually described how the House Clerk receives the information, and explains some degree of aggregation taking place such as a \$10,000 travel record not necessarily being for one trip, we know that the data release process involved relatively little aggregation. Given the emphasis in the actual use of the data on analysis of historical trends over decades, rather than on real-time watchdogging, more precise line items and more timely release do not seem to be necessary.

The disbursement records satisfied 9 of the 14 principles of open government data (some of which were not known as principles at the time the data was released), and in the cases of timeliness and documentation did so in an exemplary way.

Some of the principles that were not addressed are public input (there was no public discussion on how these files ought to have been made available), public review (there is no contact person for this data set that is made known to the public), interagency coordination (the statements might have made use of the ID scheme for Members of Congress used in other House records), and the use of safe file formats (PDFs may contain macros).

The principle of analyzability was not met either. In order to evaluate whether the disbursement statements were machine processable, one must look at the precision, accuracy, and cost of extracting the disbursement numbers out of the released PDF. The PDF contains rows of disbursements in the form of a recipient (a person or vendor, such as a telecommunications provider), a dollar amount, and various transaction codes, separated by category and in sections by congressional office. However, a PDF of tabular information provides no mechanism to search, sort, or sum. It must be converted into a spreadsheet before any analysis can be performed. PDFs vary, depending on how they were created, in the ease of extracting data out of them.

Taking the third-quarter 2009 release (the first release) as an example, copy-and-pasting a 3,397 page document into a spreadsheet program such as Microsoft Excel would have been cumbersome, and in fact would have produced garbled columns and rows in Excel. The best way to extract the information into a tabular format was an obscure use of a Unix command-line PDF processing tool,[^5] and while the resulting spreadsheet looked good, there was no way without reviewing 3,397 pages of numbers to actually know how accurate the conversion process was. Low accuracy would have been a problem, but not knowing the level of accuracy and not knowing what sorts of errors might occur is also a serious problem.

For instance, it took some insight to head off assigning disbursements to the wrong congressman. Eric Mill, a developer at Sunlight, wrote at the time, “There is no unique identifier in the data, and no standard way of formatting names of House members. Some use their nickname, some their formal name, some last names are hyphenated that shouldn’t be, other last names should be hyphenated but aren’t, etc. There are even two representatives named ‘Mike Rogers’ serving(!), and there is absolutely no way of telling the difference between the [expenditures of the] two.”[^6] This is a quite low level of accuracy.

As for precision, the variation in the naming of recipients of spending, and, additionally, the occurrences of recipients with the same name, prevent the reliable aggregation of spending by recipient. For instance, AT&T was listed under at least three names and there were 27 different names for units of Verizon. Without the ability to reliably identify which individuals are the same and which are different, it is difficult to know whether any particular line item is an aberration, and it is impossible to be confident about whether any recipient aggregate is correct. The precision of other aspects of the data, such as office and spending categories, was sufficient to make the sorts of generalizations described earlier. But the value of the remainder of the data is substantially lower because of the lack of precision and accuracy.

When I say low precision and accuracy I mean at a reasonable cost to someone performing oversight of House spending. At cost of say \$10,000, the PDF could have of course been transcribed by hand into a spreadsheet for the highest conversion accuracy, and interns could have been sent out to research the information to add precision. Not only is the cost prohibitive to anyone who might be interested in government oversight, at that rate the PDF itself becomes moot because for the same effort the same could have been done with the printed bound volumes that have been available to the public for decades. In other words, formatting of the data is key to achieving useful machine processability.

Considering the size of this data set, the ability for computers to process this information without human intervention is a critical part of its value for analysis. The data as released only nominally meet a reasonable standard of precision and accuracy within a reasonable cost. PDF is the wrong format for tabular data. A spreadsheet (whether as a plain CSV file or any other open format) would have been far preferable as it would have maintained the accuracy already present in the House Clerk’s own data files. What a PDF is good at preserving accurately is font and pagination, two aspects of House disbursements of the absolute least value. Besides the use of a spreadsheet format, the use of unique identifiers for Members of Congress and spending recipients would have dramatically improved the dataset’s quality.

[^1]: Daniel Schuman. December 21, 2010. [Keeping Congress Competent: Staff Pay, Turnover, And What It Means for Democracy](http://sunlightfoundation.com/blog/2010/12/21/keeping-congress-competent-staff-pay-turnover-and-what-it-means-for-democracy/). Sunlight Foundation.

[^2]: Lee Drutman. February 22, 2012. [Almost 400 former House staffers registered to lobby in last two years](http://sunlightfoundation.com/blog/2012/02/22/house-revolving-door/). Sunlight Foundation.

[^3]: Lee Drutman. February 6, 2012. [Turnover in the House: Who keeps - and who loses - the most staff](http://sunlightfoundation.com/blog/2012/02/06/turnover-in-the-house/). Sunlight Foundation.

[^4]: Because this analysis was cross-sectional and not longitudinal, there are two interpretations for spending that varies by time in office: 1) congressmen prefer to have more staff assistants and spend more on mail as their tenure increases, or 2) congressmen who took office in earlier decades prefer to have more staff assistants and send less mail that congressmen who are taking office today. There is no way to know from the data alone which is right.

[^5]: pdftotext with the -layout option; pdftotext was created by Glyph & Cog, LLC.

[^6]: Eric Mill. April 28, 2010. [Explore the House’s Expenditures](http://sunlightlabs.com/blog/2010/explore-houses-expenditures/). Sunlight Labs.


