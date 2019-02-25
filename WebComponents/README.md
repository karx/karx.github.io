# Web Components - For Micro-frontends and Re-usable components
Talk for MozillaPunjab

## What are Web Components?
> Web components are a set of web platform APIs that allow you to create new custom, reusable, encapsulated HTML tags to use in web pages and web apps. 

Source: https://www.webcomponents.org/introduction


> Web Components is a suite of different technologies allowing you to create reusable custom elements — with their functionality encapsulated away from the rest of your code — and utilize them in your web apps.

Source: https://developer.mozilla.org/en-US/docs/Web/Web_Components

> (Web) Components are the building blocks of modern web applications.

Source: https://developers.google.com/web/fundamentals/web-components/

```
  Insert Drawing here 
```
   

Web Components are the result of an effort by the web community to have a common specs for these 'building blocks of web'
There are two broad categories in which this can be used:
* For building __Micro-frontends__ - These are small but contains detailed buisness logic
* For building __Re-usable Components__ - These rarely contain any buisness logic. Highly targeted and re-usable components


## Basic Concepts
To understand and discuss the 3 technologies that are used to make Web components a thing, we need to first see what happens usually when a HTML page is renderd.

```
 Now we discuss about JavaScript, Browser APIs, ECMA (ES6) and polyfills
 ```
 

This page is usually what I refer to as the base: [Web Technologies](https://developer.mozilla.org/en-US/docs/Web)

I would recommend every developers, associated with Web development, to revist this page every 3 months, else the dark side WINS!


So the suit that makes web components possible is
* Custom Elements - JavaScript APIs to define custom elements and tell it to the browser.

* ShadowDOM - so that Scripting and Styling without fear of collisions

* HTML templates - \<template\> and \<slot\> elements


## Getting Started
To create a Components, broadly here are the steps we would take
* Create a Class - put your logic
* Tell the browser about this new Custom Element 
* Optional: attach Shadow DOM
* Optional: define template and then attach
* Use the new Component!


To build we have a lot of options, thanks to the uber-vibrant JavaScript community,
Our options:
* Using native JavaScript. Best source Web components by [Google Developer docs](https://developers.google.com/web/fundamentals/web-components/)
* [Polymer - Google's web components framework](https://www.polymer-project.org/) 
* [Angular Elements](https://angular.io/guide/elements)
* [Hybrids](https://github.com/hybridsjs/hybrids) is a UI library for creating Web Components with simple and functional API 
* [LitElement](https://lit-element.polymer-project.org/) - A simple base class for creating fast, lightweight web components
* [Slim.js](http://slimjs.com/#/getting-started) is a lightweight web component authoring library


In this session we will build one using - Choice