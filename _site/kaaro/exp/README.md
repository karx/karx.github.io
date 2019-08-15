## Exp to


* Procedural Generation of Video/Effects of Audio file playingf
* Buy pens++ for Munna
* 3d langton ant in a-frame
* A readme for JavaScript from https://discoverthreejs.com/book/0-intro/8-javascript-tutorial-1/



## Github Graph Query

```
query { 
  repository(owner:"xqwzts", name:"flutter_circular_chart") {
    name,
    description,
    createdAt,
    updatedAt,
    licenseInfo{
      name,
      url
    },
    owner{
      login,
      avatarUrl
    },
    mentionableUsers(first:5){
      totalCount
      nodes{
        name,
        avatarUrl
      }
    }
  }
}
```