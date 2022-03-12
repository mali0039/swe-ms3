/* eslint-disable no-undef */
/* eslint-disable max-len */
/* eslint-disable react/button-has-type */
/* eslint-disable react/jsx-no-comment-textnodes */
/* eslint-disable react/react-in-jsx-scope */
import './App.css';
import { useEffect, useState } from 'react';
import { Comment } from './Comment';

function App() {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    // eslint-disable-next-line no-undef
    fetch('/comments', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    // eslint-disable-next-line no-shadow
    }).then((res) => res.json()).then((comments) => setComments(comments.comments));
  }, []);

  const updateComment = (id, text) => {
    const allComments = [...comments];
    const idx = allComments.findIndex((ele) => ele.id === id);
    const comment = allComments[idx];
    comment.text = text;
    setComments(allComments);
  };
  const updateRating = (id, text, rating) => {
    const allComments = [...comments];
    const idx = allComments.findIndex((ele) => ele.id === id);
    const comment = allComments[idx];
    comment.rating = parseInt(rating, 10);
    setComments(allComments);
  };
  const saveComments = () => {
    // eslint-disable-next-line no-undef
    fetch('/updateComments', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(comments),
    // eslint-disable-next-line no-alert
    // eslint-disable-next-line no-undef
    // eslint-disable-next-line no-alert
    }).then((res) => res.json()).then(() => alert('Success'));
  };

  const deleteComment = (id) => {
    const allComments = [...comments];
    const idx = allComments.findIndex((ele) => ele.id === id);
    allComments.splice(idx, 1);

    setComments(allComments);
  };

  return (
    <div className="App">
      <a href="/"> Back to home </a>
      <h1> Your Comments </h1>
      <div className="comment-container">
        {comments.map((comment) => <Comment deleteComment={deleteComment} id={comment.id} updateRating={updateRating} updateComment={updateComment} text={comment.text} rating={comment.rating} />)}
      </div>
      <button onClick={saveComments}>SAVE CHANGES</button>
    </div>
  );
}

export default App;
