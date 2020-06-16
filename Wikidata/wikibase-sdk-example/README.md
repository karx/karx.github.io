## Example Using wikibase-sdk
Using cdnjs

[GitHub Repo](https://github.com/maxlath/wikibase-sdk)

## Install/Import

In page header, import using cdnjs
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/wikibase-sdk/7.6.1/wikibase-sdk.min.js"></script>
```

In your cusotm script, you can initialize the `wdk` object using `WBK`.
```
const wbk = WBK({
            instance: 'https://www.wikidata.org',
            sparqlEndpoint: 'https://query.wikidata.org/sparql'
        });
```

## Live Demo page: [Live 🐱](https://karx.github.io/Wikidata/wikibase-sdk-example)
This is hosted [index.html](./index.html) file in this directory.


## Links
* [wikibase-sdk](https://github.com/maxlath/wikibase-sdk): JS utils functions to query a Wikibase instance and simplify its results
* [cdnjs - wikibase-sdk](https://cdnjs.com/libraries/wikibase-sdk): cdnjs library page of wikibase-sdk
