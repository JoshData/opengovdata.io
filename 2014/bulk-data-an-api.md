--- 
layout: default
permalink: /bulk-data-an-api/
page_previous: /2014/data-quality/
page_next: /2014/maturity-model-for-prioritization/
title: "Bulk Data or an API?"
---
Bulk Data or an API?
====================

By Joshua Tauberer. April 2012; revised August 2014.
{: .byline }


Bulk data and APIs are the two ways open data be be published. It is important to understand when bulk data or an API is the right technology for a particular database or service.

Bulk data refers to putting all of the data into a file, or a set of files, so that all of the data can be acquired with a few simple downloads. A data API (or read-only API) is a method for providing small slices of the data. There are certain datasets that are so large (such as the Census data about every ZIP code) or so volatile (such as stock market prices that change in microseconds) that downloading it all and keeping it up to date becomes burdensome. The ability for a software developer to query for a small part of these databases can lower the barrier to entry and make it easier for developers to begin using the data.

API is an acronym[^1], but the words it stands for shed no light on what it means. An API is a contract. Not legally, but technically. It is a commitment that a system will work in a certain way. That there is a process in place. An API would say that if you visit a certain web address, you’ll get a certain slice of the data. The reason software developers have these sorts of contracts is that it provides regular rules and consistency that make it possible to build tools to automate processes. Without a commitment to a way things will work, there is no repeatable process that can be automated. In the context of government data an API often means a web-based API, but “API” refers merely to any commitment to any process.

Open data, when possible, is always both less costly to implement and more powerful than a data API:

-   Open data provides a complete database but APIs provide only a small window into the data. That means that while open data can be used to build any application, an API can only be used to build applications that require a small amount of the data at a time. The rest of the data is *not* open government data because it is not accessible.

-   Open data is static but APIs are dynamic. APIs are expected to have low response times and “high availability,” which means the service is expected to be running, and running fast, at all times. APIs require long-term maintenance to ensure that the API remains continuously and indefinitely available. Open data is released once and updated periodically as needed. (This does mean that APIs can be more timely than bulk data, which is one of the principles of open government data.)

-   A \*good\* API requires that the agency do everything that good open data requires (because ultimately it delivers the same data), plus much more. On top of good data, a well-designed API provides granular access, deep filtering, typed values, normalized tables, RESTful interfaces, multiple output formats, useful validation messages, use-case or intent-oriented URLs, documentation, client libraries, versioning, fast results, high uptime, easy on-boarding, interactive documentation, and a developer community hub.

A data API must do everything that open data does, plus much more. Therefore government agencies should walk before they run: build good open data first, validate that it meets the needs of users, learn how to do that well, and only after validation and learning invest in building an API to address additional use cases. Further, APIs alone typically do not meet the principles of open government data. APIs often require registration first (violating principle 6), and because APIs are live services “rate limiting” is usually employed to ensure that a consumer does not overly tax the underlying system. But rate limiting can also make it impossible for any single consumer to retrieve the complete dataset (violating principle 4: access in bulk).

The few cases were bulk data is not possible for information dissemination — such as when data changes in real time, like in the stock market, or when the data is extremely large — are rare exceptions to this rule.

There is *another* sort of API, however: the read-write API. Read-write refers to the ability for users not only to get (read) data but also to submit (write) data into the system. In a read-write API the external user is submitting information — such as form values — in a transactional process. Read-write APIs are an excellent strategy for the enrollment in or participation in government services. A read-write API decouples the customer’s experience from the business logic of the transaction. This permits mediators to create new experiences but still be compliant with the business logic. Just as with information dissemination, mediators can be valuable during transactions. And since transactions are by their nature dynamic, open data would not meet this need. However these sorts of APIs are beyond the scope of this book.

The prioritization of bulk data, APIs, and other aspects of open government data is discussed more in [A Maturity Model for Prioritization](/2014/maturity-model-for-prioritization/).

[^1]: for Application Programmer Interface


