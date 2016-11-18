# Short Text Mining Training Course at FPT

## Learning outcome

- Understand and practice NLP techniques for English.
- Be able to apply Web technologies to build a website.
- Learn and apply data visualization techniques to report mining results.
- Can apply security techniques to simulate Web attacks and defense.

## Project

### Task description

In the project, we will try to detect technology research trends by mining a large collection of articles related to some research topics. We can choose some topics of following topics:

- Natural Language Processing
- Big Data
- Internet of Things
- Machine Learning

### Motivations

Large amount of articles, tweets on mass media, journals, conferences, and social media about hot technologies such as Big data, Machine Learning, Internet of Things, NLP become available. Information on such medias often reflect
trends in some fields. However, for human being, it is difficult to read all
that data and get some insights about the hot trends in a field. So, it is necessary to develop automatic methods for doing that task.

### Project objectives

- Automatic mine a large collection of articles related to NLP, Big Data, Internet of Things, Machine Learning to get insights about hot trends, keywords in the fields.
- Generate, visualize a summary or report about hot trends, keywords related above fields.

### Collecting data

We would like to collect paper articles, news articles related to two topics:

- Big data
- Internet of things (IoT)

### Neccessary tools to do course project

## Schedule

(In English)

- Day 1:
  * Introduce the training course
  * Describe the project's requirements, task list
  * Assign/Discuss tasks for internship students
- Day 2:
  * Using topic modeling for mining topics/trends in raw text corpora
  * Recommended readings for topic modeling & applications for mining topics
  * Topic modeling tools
- Day 3:
  * Collecting data for the project (tech news articles about big data and internet of things)
  * Using Scrapy (Python package) to crawl data on the internet
  * Introduce some data resources for crawling raw data
  * How to processing crawled text data
- Day 4:
  * Using nltk for processing crawled text data
  * Transform text data to the data in the format of LDA tools
- Day 5:
  * Run LDA to train topic models
  * Observe outputs
- Day 6:
  * Data visualization & Make a simple website
- Day 7:
  * Review the product
- Day 8: Project demo & defense  

(In Vietnamese)

- Buổi 1: Giới thiệu về khóa học và sản phẩm được yêu cầu làm, các công việc cần chuẩn bị, thảo luận phân công nhiệm vụ của sinh viên
- Buổi 2: Giới thiệu các ý tưởng cơ bản của text mining để giải quyết vấn đề, chỉ ra các nguồn tài liệu để tự học và tìm hiểu các khái niệm liên quan
- Buổi 3: Hướng dẫn cách thu thập / crawl text (thời gian thực), các tổ chức dữ liệu text
- Buổi 4: Hướng dẫn công cụ xử lý các text đã crawl
- Buổi 5: Hướng dẫn các trích rút ra thông tin cần thiết
- Buổi 6: Xem xét và review cách trình bày thông tin ở dạng biểu đồ
- Buổi 7: Xem xét và review sản phẩm đã gần hoàn thiện
- Buổi 8: Demo sản phẩm, bảo vệ sản phẩm

## References

- David Hall, Daniel Jurafsky, and Christopher D. Manning. 2008. Studying the history of ideas using topic models. In *Proceedings of the Conference on Empirical Methods in Natural Language Processing* (EMNLP '08). Association for Computational Linguistics, Stroudsburg, PA, USA, 363-371.
- Anton Barua, Stephen W. Thomas, and Ahmed E. Hassan. 2014. What are developers talking about? An analysis of topics and trends in Stack Overflow. Empirical Softw. Engg. 19, 3 (June 2014), 619-654. DOI: [http://dx.doi.org/10.1007/s10664-012-9231-y](http://dx.doi.org/10.1007/s10664-012-9231-y).
- Bird, Steven et al. “The ACL Anthology Reference Corpus: A Reference Dataset for Bibliographic Research in Computational Linguistics.” LREC (2008).
- Priva, Uriel Cohen and Joseph L Austerweil. “Analyzing the history of Cognition using Topic Models..” Cognition 135 (2015): 4-9.
- Gollapalli, Sujatha Das and Xiaoli Li. “EMNLP versus ACL: Analyzing NLP research over time.” EMNLP (2015).
- Grant, Christan Earl et al. “A Topic-Based Search, Visualization, and Exploration System.” FLAIRS Conference (2015).
- Paul, Michael J. and Roxana Girju. “Topic Modeling of Research Fields: An Interdisciplinary Perspective.” RANLP (2009).
- Radev, Dragomir R. et al. “The ACL anthology network corpus.” Language Resources and Evaluation 47 (2013): 919-944.
- Yang, Tze-I. et al. “Topic Modeling on Historical Newspapers.” LaTeCH@ACL (2011).
- [Building an automatic keyphrase extraction system using NLTK in Python](https://in.pycon.org/cfp/2016/proposals/building-an-automatic-keyphrase-extraction-system-using-nltk-in-python~e9g4b/?ref=schedule)
- [Text Processing: Keyword-extraction](http://textprocessing.org/tag/keyword-extraction)

### Topic modeling reading list

- [Latent Dirichlet allocation in C](http://www.cs.columbia.edu/~blei/lda-c/index.html)
- [Topic Models Reading List](http://www.biasedestimates.com/p/topic-models-reading-list.html)
- [Using Gensim for LDA](http://christop.club/2014/05/06/using-gensim-for-lda/)
- [Latent Dirichlet Allocation (LDA) with Python](https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html)
- [Topic Modeling for Fun and Profit](radimrehurek.com/topic_modeling_tutorial/2 - Topic Modeling.html)
- [Topic Models Video Lecture](http://videolectures.net/mlss09uk_blei_tm/), by David Blei.
- [Topic models, large-scale learning](http://is.hust.edu.vn/~khoattq/codes.htm)
- [A Fast And Scalable Topic-Modeling Toolbox](http://www.ics.uci.edu/~asuncion/software/fast.htm)

### Web Crawling

- [Web Crawler – Python with Scrapy](http://www.treselle.com/blog/web-crawler-python-with-scrapy/)
- [Installing and using Scrapy web crawler to search text on multiple sites](https://opensourcehacker.com/2011/03/08/installing-and-using-scrapy-web-crawler-to-search-text-on-multiple-sites/)
- [Scrapy spider crawling Stack Overflow](https://gist.github.com/pawelmhm/8917867)
- [Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html)
- [Scrapy at a glance](https://doc.scrapy.org/en/latest/intro/overview.html)
- [Building a Web Crawler with Scrapy](https://blog.siliconstraits.vn/building-web-crawler-scrapy/)

### Python environments

- Try Python online: [https://repl.it/languages/python3](https://repl.it/languages/python3)
- Execute Python online: [https://www.tutorialspoint.com/execute_python_online.php](https://www.tutorialspoint.com/execute_python_online.php)

### LDA on Quora:

- [What is a good explanation of Latent Dirichlet Allocation?](https://www.quora.com/What-is-a-good-explanation-of-Latent-Dirichlet-Allocation)
- [What is the best way to explain topic modeling to a layman?](https://www.quora.com/What-is-the-best-way-to-explain-topic-modeling-to-a-layman)
- [What are good ways of evaluating the topics generated by running LDA on a corpus?](https://www.quora.com/What-are-good-ways-of-evaluating-the-topics-generated-by-running-LDA-on-a-corpus)
- [What are the best tutorial or review for studying topic modelling?](https://www.quora.com/What-are-the-best-tutorial-or-review-for-studying-topic-modelling)
- [What is a good practical usecase for Topic Modeling and LDA?](https://www.quora.com/What-is-a-good-practical-usecase-for-Topic-Modeling-and-LDA)
- [Natural Language Processing: What is the fastest and easiest to use implementation for LDA (training and inference) on a very large corpus?](https://www.quora.com/Natural-Language-Processing-What-is-the-fastest-and-easiest-to-use-implementation-for-LDA-training-and-inference-on-a-very-large-corpus)













