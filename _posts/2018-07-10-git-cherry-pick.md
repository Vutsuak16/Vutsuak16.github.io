---
layout: post
title: "Cherry Pick"
description: "Introduces cherry-picking in git"
comments: true
keywords: "git, github, version-control"
---

### Cherry-Pick ?

Cherry Picking in git is a way to include a small hotfix in our code very quickly and smoothly. For example you are working on a branch called *sign-up* , webpages loads perfecly and interacts smoothly with the database but doesnt load a new page when a person signs up. Your buddy "Kaustuv" working on another branch called *paginate* finds the solution to it and merges that as a commit in his branch.
So instead of being a layman and copy pasting his solution you can use *cherry-pick* to integrate the changes made by james's commit into your branch

### How to use it..?

First we need to find SHA-1 for Kaustuv's commit. For that we need to be in his branch
i.e. in *paginate*. So make sure we are in *paginate*

	```git checkout paginate```

Next we check the commit history and find the appropriate sha-1 for hotfix(life saving commit)

	```git log```

![command]( {{'/assets/images/command.PNG' | prepend: site.baseurl }})

We copy the appropriate commit SHA-1

Lastly we come back to our branch using checkout command and use godlike *cherry-pick*
commmand

```git cherry-pick <SHA-1>```

Voila! we have successfull merged the solution in our branch with some mean observation and three lines of code. Thanks to *Kaustuv*



### Caution

Beware of cherry picking more than one commit you might have to solve a lot of uneccessary merge conflicts and it will be an overkill. So be smart.

