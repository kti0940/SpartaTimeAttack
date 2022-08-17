function handleArticleCreate() {
    const title = document.getElementById("article_title").value
    const content = document.getElementById("article_content").value

    console.log(title, content)
    postArticle(title, content)
}