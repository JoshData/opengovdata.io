---
layout: default

page_previous: /2014/analyzable-data-in-open-formats/
page_next: /2014/permanence-trust-provenance/
title: "No Discrimination and License-Free (Principles 6 and 8)"
---
No Discrimination and License-Free (Principles 6 and 8)
=======================================================

By Joshua Tauberer. April 2012; revised August 2014, October 2014.
{: .byline }


The remaining two principles[^1] from the 8 Principles of Open Government Data state that the government may not restrict use of the data capriciously:

(6)  “**Non-discriminatory**: Data are available to anyone, with no requirement of registration.”
-----------------------------------------------------------------------------------------------

This principle is also related to the Open Definition’s “no discrimination” requirements. The [UK Open Data Whitepaper (2012)](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/78946/CM8353_acc.pdf) states the principle more clearly:

> (10) Public data will be freely available to use in any lawful way. . . . Applications are able to use the data in any lawful way without having to inform or obtain the permission of the public body concerned. . . . (11) Public data will be available without application or registration, and without requiring details of the user.

Anonymous access to the data must be allowed for public data. A requirement of registration puts data users — often government watchdogs — at risk for retaliation by the government.

### Access terms that violate the principle

Potentially discriminatory practices around data are common. Government agencies are beginning to open a door to discrimination in API terms of service agreements — contractual agreements one must agree to before accessing a live data service. For instance, to use the U.S. Energy Information Administration’s beta API a data user must agree that

> The EIA reserves the right (though not the obligation) to: (1) refuse to provide the API to you, if it is the EIA’s opinion that use violates any EIA policy; or, (2) terminate or deny you access to and use of all or part of the API at any time for any other reason in its sole discretion.[^2]

This API is potentially discriminatory if the EIA can deny access “for any other reason in its sole discretion.” In this case the same data is also available as a bulk data download for which these terms do not apply, but that wasn’t always the case. When data is *only* available through terms such as these it is not open if data users’ right to access it are dependent on an agency’s internal policies and discretions.

One dataset posted by the U.S. Substance Abuse & Mental Health Services Administration (SAMHSA) requires users to agree first:

> To use these datasets solely for research or statistical purposes and not for re-identification of specific RESEARCH SUBJECTS. . . . . . . . If SAMHSA or ICPSR determines that this terms of use agreement has been violated, then possible sanctions could include . . .[^3]

While the re-identification of research subjects may be unethical, and probably should be illegal, by narrowing permitted use to “research or statistical purposes” the agency is imposing a restriction on use considerably narrower than any lawful purpose.

Similarly, the Seattle, Washington data catalog’s terms allow the city to shut down any use of its data for any reason! Here is the relevant part of its terms of use agreement:

> reserves the right to . . . require the termination of any and all displaying, distributing or otherwise using any or all of the data for any reason[^4]

This is not open data!

Until 2014 the District of Columbia data catalog contained the same termination clause as above and required data users to “[n]otify the District of Columbia via email” about uses of DC government data.[^5] The term was dropped with the launch of the new catalog <http://opendata.dc.gov>.

See openFDA’s API [terms of use agreement](https://open.fda.gov/terms/) for an agreement that does not add capricious restrictions on use.

The second of the two principles discussed in this section is that open government data is:

(8)  “**License-free**.” Dissemination of the data is not limited by intellectual property law such as <span>copyright</span>, patents, or trademarks, contractual terms, or other arbitrary restrictions.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While privacy, security, and other concerns as governed by existing law may reasonably — and rightly — limit the dissemination of some government data, that data is not open government data. Only data not subject to a license is open. This principle is a stronger version of the Open Definition’s “redistribution” and “reuse” requirements.

[Sunlight Foundation’s Open Data Policy Guidelines (2014)](http://sunlightfoundation.com/opendataguidelines) says to “(11) Mandate Data Be Explicitly License-Free.”

This principle is also reinforced in a joint [statement](http://theunitedstates.io/licensing/) I wrote with Eric Mill (Sunlight Foundation), Jonathan Gray (Open Knowledge Foundation), Parker Higgins (Electronic Frontier Foundation), Michael Weinberg (Public Knowledge), and Timothy Vollmer (Creative Commons), and signed onto by a number of organizations: “Best-Practices Language for Making Data ‘License-Free.’ ”

A license is a contract that a data user agrees to in exchange for either a) access, or b) the right to make copies. When a work is copyrighted, a license is required to undo or partially undo the all-rights-reserved default state. This is usually the case for works created in the private sector, and it is how open source software works. Without a license, disseminating a work would be copyright infringement.

In the United States, where most federal government data is not subject to copyright[^6], there is no need for a license to make federal government data open — this data is “born” into the public domain. Any use of a license for public domain data violates the principle. But in many European countries and at the state-level in the United States, the government holds a <span>copyright</span> over works it produces[^7], though commonly with exceptions for the law itself.[^8] In jurisdictions in which government data is “born” copyrighted, a license is needed to make government data open. But in these cases the license should put the data in the public domain and not restrict access or use.

### No restrictions

For a variety of reasons, governments are imposing contractual — rather than statutory — restrictions on access or use of government data. These are licenses by another name and create new restrictions *even* when copyright law would not otherwise apply. The most common is requiring data users to agree, through a contract, to attribute (or cite) the government whenever and wherever government data is used. Also common is a data integrity requirement, which prevents data users from modifying the data. Indemnification, disclaimers of warranties, and good-conduct restrictions[^9] are also common.

It wasn’t always this way. The earliest U.S. government datasets to go online, and which remain some of the most important datasets to this day, do not have any terms associated with them whatsoever. The [U.S. Census TIGER dataset](http://www.census.gov/geo/maps-data/data/tiger.html) of state, county, and city political boundaries, the nation’s roads, and fine-grained population statistics, the [Securities and Exchange Commission EDGAR database](http://www.sec.gov/edgar/searchedgar/ftpusers.htm) of financial filings of publicly traded companies, and weather data from the [National Oceanic and Atmospheric Administration](http://www.ncdc.noaa.gov/) all are public-domain data with no legal terms attached whatsoever. These datasets were first published online in the 1990s and have been instrumental in the development of the online mapping and car navigation industries, private investing, and most weather reports we all look at each morning. Data made available by [federal legislative branch agencies](http://www.gpo.gov/fdsys/bulkdata) have never imposed terms of use. These datasets have always been license-free, and that has worked very well.

Yet many datasets now posted by U.S. government agencies, especially when posted as an API, are locked behind terms of use agreements. The SAMHSA agreement mentioned above also states:

> You agree to reference the recommended bibliographic citation in any of your publications that use SAMHSA data.

And a dataset from the Centers for Medicare & Medicaid Services (CMS) requires data users to agree that:

> The user may not present data that has been altered in any way as CMS data.[^10]

<span>Data.gov</span>, which is a catalog of U.S. government datasets, originally imposed a terms-of-use agreement on all its data sets. It read, “By accessing the data catalogs, you agree to the Data Policy,”[^11] and until 2014 its Data Policy required users of the data to include a disclaimer in their applications: “Finally, users must clearly state that ‘Data.gov and the Federal Government cannot vouch for the data or analyses derived from these data after the data have been retrieved from Data.gov.’ ”[^12]

The UK Open Government License[^13] requires data users to “acknowledge the source of the Information [and] provide a link to this licence.” In the first version of the license users were required to not “mislead others”[^14] (but this requirement was removed from the license in 2013[^15]). (This despite the [UK Open Data Whitepaper (2012)](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/78946/CM8353_acc.pdf) directing government data to use an “open license which enables re-use, including commercial re-use.”) The 2003 EU PSI Directive said that licenses covering government data in the European Union may consider “liability, the proper use of documents, guaranteeing non-alteration and the acknowledgment of source.” The <span>New Zealand Government Open Access and Licensing Framework</span>, approved in August 2010, recommends a Creative Commons license for government works that requires the data user to attribute the data back to the government:

> State Services agencies should make their copyright works which are or may be of interest or use to people available for re-use on the most open of licensing terms available within NZGOAL (the Open Licensing Principle). To the greatest extent practicable, such works should be made available online. The most open of licensing terms available within NZGOAL is the Creative Commons Attribution (BY) licence.[^16]

A cooperation of the federal and local governments in Austria in 2011 endorsed the Creative Commons Attribution License for government data as well.[^17] These guidelines do not meet the “license free” principle.

### Rationale

Requirements for attribution and data integrity, though innocuous or even beneficial sounding at first, create a lever — a civil penalty arising out of violation of a contract — by which the government can control speech. Data users agree, in virtue of reading the terms and downloading the data, to agree to the terms. When applied to medical research data, as in the SAMHSA data, this lever may seem reasonable.

But imagine these requirements on government spending data, on agency decision-making records, or government conflict-of-interest disclosure data. Would newspapers be subject to litigation for failing to attribute the government properly if the government didn’t like how the data was portrayed? Or would the public be liable for making corrections to errors in government data (altering it) before sharing it with others? What is misleading is often subject to interpretation and this sort of requirement creates a gray area for government litigation.

Here in the U.S. we have unusually, if not uniquely, strong norms about the government not interfering with public knowledge. Propaganda is illegal. Freedom of the press is incredibly strong. Requiring attribution to the government, which might sound reasonable elsewhere, would be a major policy shift with significant legal implications for the press here. “No restrictions on use” is our baseline, and transparency is impeded if accessing the information comes with restrictions on speech. The Supreme Court noted in *Citizens United* that “[d]isclaimer and disclosure requirements may burden the ability to speak.”[^18]

Making data license-free
------------------------

In the joint statement [“Best-Practices Language for Making Data ‘License-Free’ ”](http://theunitedstates.io/licensing/), my co-authors and I recommended that governments adopt specific language to put works into the world-wide public domain. For works created by federal government contractors, for instance, we recommended the following language be applied to the data:

> This work was created through a government contract which assigned copyright to [the United States Government or Agency name]. [Agency Name] waives copyright and related rights in the work worldwide through the CC0 1.0 Universal Public Domain Dedication (which can be found at http://creativecommons.org/publicdomain/zero/1.0/).

The [Creative Commons CC0](http://creativecommons.org/about/cc0) is a universal legal instrument that can be used to waive world-wide intellectual property rights in a work. Unlike the Creative Commons Attribution license, called CC-BY, the CC0 is not a license but rather a *waiver* of copyright and related rights. In jurisdictions in which a waiver is not possible, the CC0 acts as a license that grants unlimited rights in perpetuity.

The CC0 statement should be the only legal statement attached to the data. Combining CC0 and a terms of use agreement defeats the purpose of CC0.

Our recommendations also cover federal government works, primary legal materials, and works that mix government and non-government authors. Our suggested language has been used by the Department of Health and Human Services’s ckanext-datajson project[^19], the Consumer Financial Protection Bureau’s qu project[^20], and a White House report[^21]. Under White House leadership, the federal government wide CIO’s playbook now [recommends CC0 as well](https://playbook.cio.gov/#play13).

[^1]: Principle 7 was noted in [Analyzable Data in Open Formats](/2014/analyzable-data-in-open-formats/).

[^2]: <http://www.eia.gov/beta/api/tos.cfm>, accessed May 2, 2014.

[^3]: <http://www.icpsr.umich.edu/cgi-bin/terms?path=SAMHDA&study=34898&bundle=ascii&ds=1&dups=yes>, for a dataset named “1992 through 2010 Treatment Episode Data Set - Admissions (TEDS-A)”, accessed May 2, 2014

[^4]: <https://data.seattle.gov/data-policy>, accessed August 2014. Phil Ashlock says this has been unchanged since 2010 and pointed this case out to me.

[^5]: <http://data.dc.gov/TermsOfUse.aspx>, accessed August 2014. Phil Ashlock says this has been unchanged since 2010 and pointed this case out to me.

[^6]: The <span>National Institute for Standards and Technology</span> in the Department of Commerce is exempt from the no-government-copyright provision, as are often works that are produced by government contractors.

[^7]: Data, in general, is not copyrightable as such, and neither are facts, though particular compilations of data or facts may be.

[^8]: C.J. Angelopoulos writing to the OKFN’s open-government mail list on Feb. 7, 2011.

[^9]: such as agreeing not to violate the law

[^10]: The “CMS Data Disclaimer - User Agreement” linked from the dataset named [“Part B National Summary Data File - CY2001”](https://healthdata.gov/data/dataset/part-b-national-summary-data-file-cy2007), accessed May 2, 2014.

[^11]: <http://explore.data.gov/catalog/raw/>, accessed July 7, 2011

[^12]: Originally at <http://www.data.gov/datapolicy>, accessed July 7, 2011, and removed on Sept. 25, 2014, see <https://github.com/GSA/data.gov/issues/300#issuecomment-56883473>.

[^13]: <http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/>

[^14]: <http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/>

[^15]: <http://blog.okfn.org/2013/07/01/uk-open-government-license-is-now-compliant-with-the-open-definition/>

[^16]: <http://www.ict.govt.nz/programme/opening-government-data-and-information/nzgoal/read-nzgoal>

[^17]: <http://blog.okfn.org/2011/08/15/austria-adopts-ckan-and-cc-by-as-nation-wide-defaults/>

[^18]: <http://press.take88.com/wp-content/uploads/2010/03/08-205.pdf>, page 6. Unfortunately the Court dismissed the burden in their reasoning that electioneering disclosures would be reasonable.

[^19]: Because I was the contractor for HHS who built that project! https://github.com/HHS/ckanext-datajson

[^20]: https://github.com/cfpb/qu

[^21]: http://www.whitehouse.gov/sites/default/files/microsites/ostp/us\_open\_data\_action\_plan.pdf


