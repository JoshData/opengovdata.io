---
layout: default

page_previous: /2014/no-discrimination-license-free/
page_next: /2014/public-input-public-review-coordination/
title: "Publishing Data with Permanence, Trust, and Provenance (Principles 9--11)"
---
Publishing Data with Permanence, Trust, and Provenance (Principles 9–11)
========================================================================

By Joshua Tauberer. April 2012; revised August 2014.
{: .byline }


(9)  **Permanent**: Data should be made available at a stable Internet location indefinitely.
-------------------------------------------------------------------------------------------

Providing documents with **permanent web addresses** helps the public share documents with others by allowing them to point others directly to the authoritative source of the document, rather than having to provide instructions on how to find it, or distributing the document separately themselves. Permanent locations are especially useful on government websites which are prone to being scratched and re-created as political power shifts. The <span>American Association of Law Libraries</span>’ principles call permanent addresses “persistent URLs (PURLs)” — although <span>PURLs</span> are usually short-URLs that can be updated at any time to redirect to the current location of a resource. The use of redirecting URLs should be a last resort when a persistent, descriptive URL cannot be created.

When data changes over time, persistence means 1) retaining copies of all published versions of the data, and 2) maintaining stability of format from version to version. Changes to a data format should strive to be backwards compatible and use a two-stage deprecation process: warn first, then change.

- - -

The <span>Association of Computing Machinery</span>’s [Recommendation on Open Government](http://www.acm.org/public-policy/open-government) (February 2009) included two other unique principles:

(10)  **Safe file formats**: “Government bodies publishing data online should always seek to publish using data formats that do not include executable content.”
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Executable content within documents poses a security risk to users of the data because the executable content may be malware (viruses, worms, etc.).

Even with anti-virus software installed, malware is spread easily through file formats that contain natively executable code (.exe’s on Microsoft Windows), macros with full access to the user’s computer (Microsoft Office documents with macros enabled), and in rarer cases formats that permit scripting languages (PDFs) because such formats are prone to bugs. In many cases the best protection for a user is to simply not open files that may contain executable content. Governments should not ask a user to choose between their security and access to government information, and so open government data should avoid these formats.

The most common violation of this principle has been the use of Microsoft Office documents with macros. These macros were once a widely used method of spreading computer viruses. This is rarer today, in part because of more useful security settings available in Microsoft products, and in part because since Microsoft Office 2007 documents with macros are saved in .–m files (.docm, .xlsm). The new file naming convention ensures document creators and document users can be sure that their files do not contain executable content. Documents that end in .–x (.docx, .xlsx) do not contain executable content and therefore satisfy the principle of safe file formats.

It is not widely known that the PDF format may contain executable content in the form of Javascript. Malware has been spread through Javascript in PDFs.[^1] While it is of course possible to create a PDF without Javascript, the user opening the document has no way to know whether any particular PDF is safe before opening it — by which point it may be too late. I am hesitant to call PDF an unsafe file format because of its enormous value for other reasons and the low incidence rate of PDF malware. But it cannot be called a safe file format.

(11)  **Provenance and trust**: “Published content should be digitally signed or include attestation of publication/creation date, authenticity, and integrity.”
--------------------------------------------------------------------------------------------------------------------------------------------------------------

A digital signature is a method to ensure that, byte for byte, the data you have is the same as the data as published by its source. Digital signatures help data users validate the source of the data they find so that they can trust that the data has not been modified since it was published. Establishing provenance and trust in a machine-processable way is important for static information. This is sometimes called authenticity or authentication.

Authenticity has been emphasized lately primarily by the government document librarian community, and digital signatures are now a primary offering of the Government Printing Office’s FDSys database of federal government documents. Authenticity is also a core component of the Uniform Electronic Legal Materials Act movement[^2].

There are two significant reasons to beware of the significance of authenticity, however:

An often heard claim is that governments have a responsibility to use digital signatures to prevent government documents from being (illicitly) modified. This is not correct. Since it is the transformation of data into new forms by mediators that makes government data useful to citizens, modification *is the point*. (And it has always been this way. See the discussion of mediators in [Open Government, Big Data, and Mediators](/2014/open-government-big-data-mediators/).) On my website GovTrack.us, I modify congressional data in every way that I present it to make it more accessible, informative, and actionable by my users — without making the presentation any less accurate. (GovTrack.us has bugs, but so does government data!) In this way digital signatures stand in contrast to the principle of analysis.

(There is unfortunately no method for a digital signature to be preserved when data is modified. Adaptations of data, analyses, visualizations, and corrections and cleanups to data necessarily change the bytes or add new bytes, breaking the digital signature.)

Additionally, non-technical users of government documents may not know how to properly validate a digital signature. While some software applications can validate digital signatures for users, such as Adobe Acrobat for PDF files, the simplicity offered by these applications can give a false sense of security. These programs are incredibly difficult to use properly, even by technologists. We are a long way from being able to teach citizens to recognize when a file *hasn’t* been digitally signed by a trusted authority.

The responsibility governments do have is ensuring that those who want original government documents — the mediators themselves, archivists, researchers, and enterprising citizens — can in fact get them now and in the future. Digital signatures should be a part of government information dissemination and preservation but should not hinder dissemination or prevent the analysis and reuse of government data.

[^1]: <http://www.symantec.com/connect/blogs/rise-pdf-malware>

[^2]: <http://www.mnhs.org/preserve/records/legislativerecords/authentication.php>


