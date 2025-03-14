![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# LAB | Web Scraping
<details>
  <summary>
   <h2>Learning Goals</h2>
  </summary>

  This lab allows you to practice and apply the concepts and techniques taught in class. 

  Upon completion of this lab, you will be able to:
  
- Understand the basics of **web scraping** using Python.
- Extract information from **HTML documents** using `BeautifulSoup`.
- Use key methods to parse HTML: `find`, `find_all`, `text`, `get_text`, `get`, and `select`.
- Retrieve specific elements from an HTML document, such as titles, paragraphs, and links.

  <br>
  <hr> 

</details>

<details>
  <summary>
   <h2>Prerequisites</h2>
  </summary>

Before starting this lab, you should have knowledge of:

- Python Programming
- Basics of HTML structure and tags
- Introduction to `BeautifulSoup` for parsing HTML
- Basic use of methods such as `find`, `find_all`, `get_text`, and `select`

  <br>
  <hr> 

</details>

## Introduction

Welcome to the **Web Scraping** lab! In this lab, you will learn how to extract information from HTML documents using `BeautifulSoup`. Web scraping is a powerful technique used to collect data from websites, and it is widely used in **data analysis, automation, and research**.

By the end of this lab, you will have hands-on experience with fundamental scraping techniques, such as retrieving **text, links, and HTML elements**. You'll also practice using common `BeautifulSoup` methods to filter and extract relevant information.

Let’s get started! 🚀

---

## Important Notes

This lab builds upon **Python programming concepts**. If you are unfamiliar with HTML structure and `BeautifulSoup`, review the related materials or ask your TA for additional guidance.

---

## Requirements

- Fork this repo
- Clone it to your machine

## Getting Started

Complete the challenges in the `Jupyter Notebook` file. Follow the instructions and add your code and explanations as necessary.

---

## Instructions

You will work with the following **HTML document**:

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from
w3resource.com</a></p>
</body>
</html>
"""