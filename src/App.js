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
      }}).then(res => res.json()).then(comments => setComments(comments.comments))
  }, [])

  return (
    <div className="App">
      <h1> Your Comments </h1>
      <div className="comment-container">
      {comments.map((comment) => <Comment setComments={setComments} text={comment.text} rating={comment.rating} />)
      }
      </div>
      <button onClick={ () => console.log(comments)}>CLICK</button>
    </div>
  );
}

export default App;
