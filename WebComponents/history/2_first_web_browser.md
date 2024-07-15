---
title: "The Web’s First (And Second) Browser"
players:
    - Tim Berners-Lee, CERN
    - Nicola Pellow (Intern)

date:  December 25, 1990
---

 
 WorldWideWeb, the first browser ever conceived and by the creator of the web no less, was not just a browser, but also a web editor.


 libwww was an API package meant to be a starting point for developers building browsers


The libwww library (previously known as the Common Library) acted as a much-needed catalytic spark in the earliest days of the web. Developed in 1992 by the creator of the web, Tim Berners-Lee, libwww was an API package meant to be a starting point for developers building browsers, itself derived and chunked out from a browser Berners-Lee was working on at the time. It wasn’t long before programmers, clustered together in small groups or working on their own, started downloading the package and hacking together browsers for their platform of choice. Because of the release of libwww, in just under a year, half a dozen new browsers were created for the web, available for Windows, Mac and several different Unix variations.

Not bad for a library that was just a side effect of the first browser ever made.
The Line Mode Browser

There wasn’t some singular vision for the web. It was accessible to all and disjointed by design, and its development happened only through the parallel efforts of curious programmers around the world. But in order to even access the web (and experiment with it), early adopters needed a client, software that could use HTTP to grab a URI and display HTML. In other words, a web browser. Most used the Line Mode Browser. It was the second browser ever made.

The Line Mode Browser was built by Nicola Pellow in May of 1991. At the time, Pellow was still just an intern at CERN, but she had shown a passion for the web and Berners-Lee entrusted her with the project. Her goal with the Line Mode Browser was to create something versatile, flexible, and interoperable. What she ended up with was a text-only, grayscale browser that could only be accessed via the command line and required at least rudimentary knowledge of computer science to even get installed. But even though it was about as basic as you could get, it became incredibly popular.

Its simplicity actually gave it an edge. The Line Mode Browser was easy to use (once you got it setup) and more importantly, easy to modify (hack) so that it could be bent to any purpose. It could quickly access any web page with just a few commands, even if the page itself was black and white and a little boring.  At its core, the Line Mode Browser offered a no-nonsense way to read web documents, which is really all anybody was asking for at the time. That will make a lot more sense once we get to the phonebook.

The Line Mode Browser UI
Stepping Back

At the time though, there was one other option. It was called WorldWideWeb and actually predated the Line Mode Browser by about a year. It was created by Berners-Lee at around the same time he came up with the web itself. The World Wide Web built on a lot of great technologies that had come before it, and Berners-Lee kind of mixed together Internet best practices and a few bright new ideas to make it happen. But he still didn’t quite know how the web was going to feel. So the WorldWideWeb browser became a place where Berners-Lee could test out new ideas and experiment with possible interfaces. It became his programatic canvas, a way for him to sketch out what the web would become.

The first kind of striking thing about WorldWideWeb is that it was a graphical browser. It would be a couple of years before anyone came back around to that. Then there was the browser chrome: an address bar, a back button and a way to organize browser windows. And unlike the Line Mode Browser, it featured (admittedly primitive) styling of HTML elements, inline images, and spell checking. There was even a whole bunch of nifty keyboard and UI shortcuts for users to explore.

Screenshot of WorldWideWeb browser

But the showstopper was that it was a read / write browser.

So WorldWideWeb, the first browser ever conceived and by the creator of the web no less, was not just a browser, but also a web editor. You could use it to edit HTML documents on your local computer and then push files via FTP up to a server. That reveals a lot about Berners-Lee’s early vision of the web. When he looked toward the technology’s future he saw websites as open, editable destinations where users interacted with one another. He wanted to build a digital space not just of consumption but of creation as well.

Unfortunately, the WorldWideWeb browser never really caught because it only worked on NeXT computers.
Back to the Phonebook

Web browsers more or less started with a phonebook.

Berners-Lee was an employee at CERN (The European Organization for Nuclear Research) when he pitched the idea of the world wide web. CERN is a particle physics lab best known for things like the Large Hadron Collider and generally not all that concerned with hypertext or the Internet. So to actually get the project approved, Berners-Lee and his boss, Mike Sendall, had to come up with a clever corporate cover.

Sendall knew that what CERN actually did need was a corporate directory. Employees were spread around the globe, and that made it difficult find a reliable address and phone number for a given employee. A corporate directory that was accessible through the Internet was an appealing proposal. So even though Berners-Lee had big dreams for the future of the web, his original work with with hypertext and URI’s and HTTP was done under the guise of “really advanced phonebook.”

This was around the same time that the NeXTcube was launched. Steve Jobs had founded the NeXT computer company after being ousted from Apple. The NeXTcube was their most advanced model. It was fast, powerful, and extremely expensive. Sendall and Berners-Lee managed to convince their superiors that it was a computer worth at least checking out to see what kind of utility it could provide.

Which helps to explain some of the more advanced features that went into the WorldWideWeb browser. Berners-Lee called NeXT the “ideal prototyping platform,” and with good reason. Under the hood it was surprisingly easy to create software for and gave developers access to low level graphical components and rendering tools. Creating a proper GUI for his browser took very little time, leaving plenty of bandwidth to devote to code editing features. In about two months, Berners-Lee finished up the first version of WorldWideWeb.

But remember, the original pitch for their clandestine phonebook application was that it could be used by any employee anywhere. WorldWideWeb was built for, and only worked on, NeXT computers, not a particularly popular operating system. Running close to out of time on the project, Berners-Lee recruited Nicola Pellow to build something simpler and more accessible. In about a month, Pellow had created the Line Mode Browser. And even though it lacked just about every major feature of WorldWideWeb, it could be downloaded and installed on any operating system. Which is all you ever really needed to access a phonebook on the Internet.
CERN directory on the web
A phonebook that looks like this

By mid-July of 1991, Berners-Lee realized that WorldWideWeb (by then renamed to Nexus to avoid confusion with the original project) was just never going to catch on. So rather than lose everything, he took the best bits of the browser and ported them over to interoperable modules written in the C programming language. That package was called libwww, and it piqued the interest of more than a few developers who in turn began to hacking together the next generation of browsers.

One of the first stories of the web brings along with it some enduring lessons. The first is, browsers will always be in a race to get things shipped. You can’t build a user base on the strength of just an idea. Fundamentally, that’s why the Line Mode Browser won out in the beginning. The other is that the web is an open platform, and its development is almost wholly contingent on a group of strangers from around the world building things both in isolation and together. That’s what the web was made from.