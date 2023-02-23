# Welcome 

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.

## Usage

### Using annotations

[:octicons-heart-fill-24:{ .mdx-heart } Sponsors only][Insiders]{ .mdx-insiders } ·
[:octicons-tag-24: insiders-4.6.0][Insiders] ·
:octicons-beaker-24: Experimental

Annotations consist of two parts: a marker, which can be placed anywhere in
a block marked with the `annotate` class, and content located in a list below
the block containing the marker:

``` markdown title="Text with annotations"
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.
```

<div class="result" markdown>

Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

</div>

# Hello World

## Hello there

<div class="grid cards" markdown>

- **Dive into :material-docker:{ .docker .lg .middle } [Docker Swarm](/docker-swarm/design/)**

    ---

    The quickest way to get started, and to get your head around the basics.

- **Kick it with :material-kubernetes:{ .kubernetes .lg .middle } [Kubernetes](/kubernetes/)**

    ---

    Been around for a while? Got a high pain threshold? Jump in!

- **Geek out in :fontawesome-brands-discord:{ .discord .lg .middle } [Discord](http://chat.funkypenguin.co.nz)**

    ---

    Join the fun, chat with fellow geeks in realtime!

- **Fast-track with 🚀 :brain: :laughing: [Premix](/premix/)!**

    ---

    Life's too short? Fast-track your stack with Premix!

</div>

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

