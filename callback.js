const posts = [
    {
        title: "Post 1",
        body: "This is Post 1"
    },
    {
        title: "Post 2",
        body: "This is Post 2"
    }
]

const getPosts = ()=>{
    setTimeout(() => {
        let output = ""
        posts.forEach(post => {
            output+=`<li>${post.title}</li>`
        })
        document.getElementById("list").innerHTML = output
    }, 1000);
}

const createPost = (post, callback)=> {
    setTimeout(() => {
        posts.push(post)
        callback()
    }, 2000);
}



let post = {title: "Post 3", body: "This is Post 3"}



createPost(post, getPosts)