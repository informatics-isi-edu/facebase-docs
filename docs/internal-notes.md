
Links should be set up as follows:

Path to images:
```
{{ "/assets/img/data-key-concepts.jpg" | relative_url }}
```
Links to other pages:
```
{{ "/docs/Data-Submission-Process/" | relative_url }}
```

Changing links from wiki to site:

Move page links from:

(./Data-Submission-Process)

to

({{ "/docs/Data-Submission-Process/" | relative_url }})

Move image links from:

(images/data-key-concepts.jpg)

to

({{ "/assets/img/data-key-concepts.jpg" | relative_url }})
