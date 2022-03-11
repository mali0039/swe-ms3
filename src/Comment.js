import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

export function Comment(props) {
  const [commentText, setCommentText] = useState(props.text);
  const [rating, setRating] = useState(props.rating);
  const [id] = useState(props.id)

  function updateCommentText(text) {
    setCommentText(text); 
    props.updateComment(id, text, rating);
    
  }
  function updateRating(newRating) {
    setRating(newRating); 
    props.updateComment(id, commentText, newRating);

  }
  return (
    <div >
      <form className="comment" action="/comment" method="POST">
        <label htmlFor="comment">Comment</label>
        <input minLength="3" maxLength="100" type="text" name="comment" onChange={(e) => updateCommentText(e.target.value)} value={commentText} />
    
        <label htmlFor="rating">Rating</label>

      <select name="rating" onChange={(e) => updateRating(e.target.value)} value={rating}>
        {[...Array(10)].map((x, i) =>
          <option value={ i+ 1}>{ i+ 1}</option>
        )}
      </select>
    </form>
      </div >
  );
}

