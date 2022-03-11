import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { Comment } from './Comment';
function App() {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetch("/comments", {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    }).then(res => res.json()).then(comments => setComments(comments.comments))
  }, [])

  const updateComment = (id, text, rating) => {
    let allComments = [...comments];
    let idx = allComments.findIndex((ele) => ele.id == id);
    let comment = allComments[idx]
    comment.text = text;
    comment.rating = parseInt(rating)
    setComments(allComments);
    console.log(allComments)
  }
  const saveComments = () => {
    console.log("CLICKED");
    fetch("/updateComments", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(comments)
    }).then(res => res.json()).then(res => alert("Success"))
  }
  return (
    <div className="App">
      <h1> Your Comments </h1>
      <div className="comment-container">
        {comments.map((comment) => <Comment id={comment.id} updateComment={updateComment} text={comment.text} rating={comment.rating} />)
        }
      </div>
      <button onClick={saveComments}>SAVE CHANGES</button>
    </div>
  );
}

export default App;
