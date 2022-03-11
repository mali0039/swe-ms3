import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

export function Comment(props) {
  const [commentText, setCommentText] = useState(props.text);
  const [rating, setRating] = useState(props.rating);

  // useEffect(() => {
  //   fetch("/comments").then(res => res.json()).then(comments => setComments(comments.comments))
  // }, [])
  function updateComment()
  return (
    <div >
      <form className="comment" action="/comment" method="POST">
        <label htmlFor="comment">Comment</label>
        <input type="text" name="comment" onChange={(e) => {setCommentText(e.target.value); props.text(e.target.value)}} value={commentText} />
    
        <label htmlFor="rating">Rating</label>

      <select name="rating" onChange={(e) => {setRating(e.target.value); props.rating(e.target.value)}} value={rating}>
        {[...Array(10)].map((x, i) =>
          <option value={ i+ 1}>{ i+ 1}</option>
        )}
      </select>

      <button type="submit">Save</button>

    </form>
      </div >
  );
}

