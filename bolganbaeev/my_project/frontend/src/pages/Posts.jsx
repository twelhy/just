import { useEffect, useState, useRef } from 'react'
import { getPosts } from '../services/api'
import '../App.css'


function Posts() {
  const [posts, setPosts] = useState([]);
  const calledRef = useRef(false);

  useEffect(() => {
    if (calledRef.current) return; // егер бұрын шақырылған болса, қайталауды болдырмау
    calledRef.current = true;

    getPosts().then(data => {
      if (data === 404) {
        setPosts([{ id: 1, title: "Error: 404", content: "Sorry, try later." }])
      } else {
        setPosts(data)
      }
    })
  }, [])


  return (
    <>
      {posts.map(p => (
        <div key={p.id}>
          <h3>{p.title}</h3>
          <p>{p.content}</p>
        </div>
      ))}
    </>
  )
}

export default Posts;
