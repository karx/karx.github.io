---
title: "Protocols | URL"
players:
    - Tim Berners-Lee 

link: http://info.cern.ch/hypertext/WWW/TheProject.html

date:  1992
---
Their jobs are also remarkably similar to that of a domain name server. And domain names are very important for the URL and, by extension, the web.

That’s what we’re talking about today.

I’ll come back to domain name servers. First, we have to take a look at domain names. Domain names are what you type into the address bar of your browser of choice (historyoftheweb.com for instance) to connect to a website. But each domain name actually corresponds to a matching IP address, a series of numbers assigned to any computer tethered to the Internet. That’s actually true of all of our personal computers, though our own IP addresses are likely shifting all the time behind the scenes thanks to a technology known as DHCP. Web servers are far more likely to have a static IP address, a number pattern that changes only in rare circumstances. Amazon.com, for instance, has an IP address of 176.32.98.166.

Machines can read and interpret IP addresses just fine. The problem is, humans are incredibly bad at remembering a series of numbers. We are much, much better at remembering names. So we had to build a system that reconciled the two, that matches every server’s machine-readable IP address with its human-rememberable domain name.

The first domain names came out of the ARPANET project, an early precursor to what would eventually become the Internet. In the early days, information scientist Elizabeth Feinler was responsible for keeping track of every single computer on the network. Most of the computer’s belonged to individual people, so Feinler maintained a single directory that mapped each computer to its owner. This was originally stored in an extremely long hardcopy document, but was later ported to a virtual server known as WHOIS (a name that likely sounds familiar to a few of you developers).

In the mid-80’s, as ARPANET transitioned from a government research project to what we know now as the Internet, it was decided that a more robust way to name computers connected to the network was needed. One of the key insights of the Internet was the addition of the machine-friendly IP address, but Feinler and several other researchers realized that connecting directly to IP addresses wouldn’t be sustainable in the long run. They began working on a standard for a more human-friendly naming system.

They settled on something simple and versatile: a domain followed by a host, separated by a period. Each host could be named in any way that domain saw fit, as long as every host on the domain stuck to the same conventions. The original proposal for domain names included seven top-level domains. They were .com, .net, .gov, .edu, .org, .mil, and .int. The host + domain standard were called domain names. The theory was, by connecting to a domain name (i.e. thehistoryoftheweb.com) you could easily get wherever you needed to go on the Internet without having to remember a complex series of numbers and periods.

Now all that was needed was a way to connect domain names to IP addresses. Which brings us right back around to domain name servers. This process is known as the Domain Name System, or DNS, and the technology that powers it is quite interesting. The details are a bit complex, but this is basically how it works.

When you type a domain name into your browser, it makes a request to a domain name server, an Internet connected computer that contains (to simplify a bit) a giant list of domain names matched to IP addresses, a virtual Elizabeth Feinler essentially. However, the system is built to be redundant and decentralized for incredibly technical reasons. So that no one domain name server can act as a single point of failure, none are entirely complete. Instead, the list is distributed through clusters of servers all around the world, each with a partial copy of the full list.
A rough diagram of DNS

When a browser makes a request for a domain name, it contacts the nearest domain name server to see if it has the matching IP address. If that server is unable to find the IP, it passes the request along to another domain name server. Then to another. Then another.

If that feels a lot like the switchboards from the telephones of yesteryear, that’s because it is derived from the same system. Each domain name server acts like its own telephone switchboard operator, patching the connection through with a single connection if they can, and passing the signal along to another operator if they can not. Just like Princess Margaret trying to make an international call to Buckingham Palace. In some cases, these connections even make their way to a Root Name Server, 13 unique server clusters hosted around the world that are responsible for keeping the master list of each top-level domain.

The domain name predates the web by a good 20 years. Still, it is pretty important for the Uniform Resource Locator (URL). Along with HTML and the HTTP protocol, the URL is one of the three foundational technologies of the web. Tim Berners-Lee once said this of the URL:

    [The URL] is the most fundamental innovation of the Web, because it is the one specification that every Web program, client or server, anywhere uses when any link is followed.

The web is nothing without the hyperlink. The connection between websites is at the center of the web’s ideological and technological roots. Indeed, the spread of the World Wide Web would have been far less revolutionary if it was not possible to link one website to any other. But in order for hyperlinks to even exist, each and every page on the web needed to have a single address. Two houses can’t have the exact same postal address, or we’d never be able to find anything. The same is true of webpages. The URL solved that by offering a web address that was standardized, easy for browsers to understand, simple for web authors to add to their own sites, and most importantly, unique.

Berners-Lee chose to mix and match a few different technologies and conventions for the URL, and each separate piece of the URL is separated by a series of slashes (/). The first bit of a URL will likely make sense to some of of you. It defines the protocol in use, typically http: or https:, but it leaves room for less traditional protocols, like ftp: or gopher:.

But why the (totally optional) www? If anyone remembers the first years of the web, they likely recall telling a friend to go to “double-u double-u double-u dot google dot com“. When the web was young, the www was almost always part of a URL. In recent years, it has mostly fallen off. As it turns out, this was never a standard, and was simply a convention of the early web. At the time, with so many ways to connect to the Internet, a website was just one piece of a larger private or public server. The www subdomain was a way of carving out a piece of the a server and making it available to the web. Since most servers are dedicated to just websites these days, the convention is really no longer necessary. Of course, without the flexibility of the URL, that would never have been possible.
The anatomy of a URL, courtesy of Sitechecker.Pro

This is, of course, followed by a series of slashes that represent a particular location on a domain (i.e. /about, /timeline), which was adopted by Berners-Lee from the Apollo computer, a now defunct workstation and operating system. It was up to individual webmasters to define what the information after that / actually means, but in general it’s come to mean a directory structure much like the paths to folders on each of our computers.

With all of those pieces cobbled together, the URL was complete. It’s an amazingly simple and essential piece of technology. Chances are, you don’t think about it all that much. But without a unique URL for every location on the Internet, and the various influences and technologies that enabled its existence, we wouldn’t have the World Wide Web at all. We’d just have a mess of unidentifiable information.