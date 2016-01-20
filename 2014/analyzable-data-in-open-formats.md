---
layout: default

page_previous: /2014/online-free-primary-timely-accessible/
page_next: /2014/no-discrimination-license-free/
title: "Analyzable Data in Open Formats (Principles 5 and 7)"
---
Analyzable Data in Open Formats (Principles 5 and 7)
====================================================

By Joshua Tauberer. April 2012; revised August 2014.
{: .byline }


Data should be analyzable and in non-proprietary formats.

(5)  **Analyzable**.
------------------

The most critical value of open government data comes from the public’s ability to carry out its own analyses of raw data, rather than relying on a government’s own analysis. The principle that open government data is analyzable is truly the core of open government data. It has been stated in many different ways:

In the original words of the 8 Principles: “5. Machine processable: Data are reasonably structured to allow automated processing.” In the [UK Open Data Whitepaper (2012)](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/78946/CM8353_acc.pdf): “(2) Public data will be published in re-usable, machine-readable form.” In [Sunlight Foundation’s Open Data Policy Guidelines (2014)](http://sunlightfoundation.com/opendataguidelines): “(8) Mandate Data Formats For Maximal Technical Access.”

The <span>Association of Computing Machinery</span>’s [Recommendation on Open Government](http://www.acm.org/public-policy/open-government) (February 2009) stated the same principle another way: “Data published by the government should be in formats and approaches that promote analysis and reuse of that data.”

The goal of this principle needs some unpacking. Before the 8 Principles of Open Government Data were published, the term I heard most often for this was “<span>machine readable</span>.” At the workshop, Aaron Swartz pointed out that any data can be read by a machine and that it is not the reading of the bytes that is important to openness but whether the machine can usefully process it. The group adopted “processable” instead. The machine-processable principle is important because as the sizes of data sets grow, the most interesting, informative, or innovative applications of government data require the use of a computer to search, sort, or transform it into a new form. Most broadly, this is analysis.

But as powerful as computers are, they don’t work well with uncertain data. For instance, human language is remarkably uncertain at least from the point of view of the computer. It doesn’t know what any of this text means. Prose to a computer is like <span>poetry</span> to me. I just don’t get poetry. When I read a poem I need someone to explain to me what it means and how it is meant to be interpreted. And so it is for a computer. There is no meaning to a computer besides what a programmer gives it. Give a computer audio or images and without the proper software a computer is like an octopus suddenly relocated into the middle of Times Square. Its mind could not begin to make sense of the signals coming from its eyes. (The refined octopus would ask of Times Square “why?”, but your common octopus would have no idea what is going on.) Think of how each type of computer file can be opened only in the software it was meant for: Microsoft Word documents are opened in Microsoft Word, PDFs are opened in Adobe Acrobat, and so on. Data is nothing without the ability to create software to process it.

Sometimes government data falls into a category for which there is an appropriate, standard data format — and corresponding application. Tabular data, such as spending data, can be saved into a spreadsheet format (e.g. Microsoft Excel or, better, the CSV format). Saving it in this format, compared to a scanned image of the same information, creates certainty. Programmers know how to make programs that work reliably with numbers in rows and columns. Software already exists for that. There is no reliable way to work with the same information when stored in a scanned image.

But other government data doesn’t fit into a standard data format. When the relationships between things encoded in the data become hierarchical, rather than tabular, it is time to think about using a dialect of XML. For instance, an organizational chart of a government department is hierarchical and would not fit nicely into a spreadsheet. The information could be typed into a spreadsheet, but whether *you* can figure out how to interpret such a spreadsheet and whether a *computer* has been programmed to interpret and process it are not the same. Much like the difference between poetry and prose, the use of an incorrect format can render the data completely opaque to software that could process it.

The principle of machine processability guides the choice of file format — free-form text is not a substitute for tabular and normalized records, images of text are not a substitute for the text itself — but it also guides how the format is used. When publishing documents it is important to avoid scanned images of printed documents even though scanned images can be included in a PDF, and PDF is a recommended format for certain types of documents. A scanned image is an uncertain representation of the text within it. An RSS or Atom feed of a schedule encodes dates and times with certainty, but it does not provide a way to include a meeting’s location or topic in a way that a computer could meaningfully process. If those fields are important, and that will depend on what will be done with the feed, then the feed will need to be augmented with additional XML for that purpose.

XML is best thought of as a type of data format, rather than a particular format. There are many ways to apply XML to any particular case, and the choices made in applying XML should continue to be guided by the principle of machine processability.

Machine processability also implies that the data should be clean. The smallest of mistakes in the data can dramatically increase the cost of use of the data because fixing mistakes almost always requires human intervention: making the data not machine-processable. This isn’t to say the data must be correct. Data that has been collected, e.g. a survey or a measurement, can be reported as it was collected when it has uncorrectable errors or when correction involves judgment. Data is clean when its data format has been appropriately applied and when its values are normalized.

Machine processability is closely related to the notion of data quality. For more, see [Data Quality](/2014/data-quality/).

Next I skip ahead to principle 7 from the 8 Principles of Open Government Data:

(7)  “**Non-proprietary**: Data are available in a format over which no entity has exclusive control.”
----------------------------------------------------------------------------------------------------

Proprietary formats add unnecessary restrictions over who can use the data, how it can be used and shared, and whether the data will be usable in the future. While there is nothing wrong in principle with exclusive control over a data format, proprietary formats are troublesome for open data because data is not open if it is not open to all.

A document released for the word processing application Pages will only be open to individuals who can afford to own a Macintosh computer. It can only be used in ways supported by the Pages program. And looking ahead, since government documents should be archivable, it will only be able to be opened so long as the company Apple still exists and continues to support its Pages application. Proprietary formats create practical restrictions that open, non-proprietary formats do not. Non-proprietary formats are often supported by a wider range of applications, and therefore support a wider range of uses and users.

Writing in 2012, Kevin Webb of OpenPlans encountered a problem using geospatial (GIS) data considered nominally open from the U.S. Geological Survey. He wrote:

> Several weeks back I needed to make a map for a big chunk [of] the Pacific Northwest. I leveraged all kinds of useful open data (OSM for streets, Lidar from local governments, etc.) but above all else I needed really good stream and river data. Lucky for me the USGS maintains a detailed data set that maps every stream and pond in the entire U.S., even the tiny intermittent ones!
>
> I’ve been working with GIS tools and data in a professional capacity for going on fifteen years and I consider myself pretty savvy. However, over the last decade all of my work has come to depend on open source GIS tools—my ArcGIS license and the parallel port dongle it required stayed behind when I left university. So while I can tell you all about spatial indexes and encoding formats for transmitting geometric primitives, I missed the memo on ESRI’s new File Geodatabase format; the format now being used to manage and disseminate data at the USGS.[^1]

The new Geodatabase format has become the standard data format for GIS information, replacing the open Shapefile format, Webb wrote. Unfortunately, the only software capable of opening Geodatabase files is the software produced by the company who created the format, ESRI, which sells its software for \$1,500. There is nothing wrong with ESRI keeping its formats proprietary to induce potential buyers to pick up its software. But the USGS’s choice to use a proprietary format reduced the value of the data to the public substantially.

Use of proprietary formats may also constitute a form of endorsement that may create a conflict of interest. While some proprietary formats are nearly ubiquitous, it is nevertheless not acceptable to use only proprietary formats, especially closed proprietary formats. On the other hand, the relevant <span>non-proprietary formats</span> may not reach a wide audience. In these cases, it may be necessary to make the data available in multiple formats.

### Recommended file formats

The choice of <span>file format</span> involves a consideration of both access and machine processability. For <span>tabular data</span> such as <span>spreadsheets</span>, CSV (“comma separated values”) is the most widely usable format.[^2] It is simply a text file with commas delimiting the columns. In the case of tabular data, simplicity is key.

There is no one answer for the appropriate file format for <span>documents</span> because of two often competing requirements: being print-ready (e.g. including pagination, layout, etc.) and encoding the content in a machine-processable way. The PDF format is always print-ready (PDF/A-1b is the specific minimum requirement for documents that need to be archived), but PDF normally does not make the information contained in the document machine-processable.[^3] It is therefore necessary in some cases to publish a document in two formats simultaneously, once in a format like PDF to satisfy the needs of printing and once in a format such as XHTML or XML.

Although the PDF format was originally proprietary, it has since been taken over by a standards body making it an open, non-proprietary format. Microsoft Office’s Word file format and OpenOffice’s OpenDocument format are print-ready like the PDF format but also allow for reliable text extraction, making them better formats for open government data than PDF in most cases.[^4] But neither PDF nor Word nor OpenDocument is a substitute for good data in XML.

[^1]: <http://www.structuralknowledge.com/2012/02/03/why-esri-as-is-cant-be-part-of-the-open-government-movement/>, accessed Feb. 6, 2012.

[^2]: CSV has not been well standardized. When using CSV, it is best to include a header row, use quotes around fields where needed, and use UTF-8 character encoding. For more, see my proposal for uCSV at <http://razor.occams.info/pubdocs/ucsv.html>.

[^3]: While “Tagged PDF” (PDF/A-1a) could achieve both goals simultaneously, most software that supports PDF output does not adhere to PDF/A-1a.

[^4]: The current Microsoft Office file formats are non-proprietary. The old version 6 formats were proprietary.


