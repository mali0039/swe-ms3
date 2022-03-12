/* eslint-disable react/button-has-type */
/* eslint-disable jsx-a11y/label-has-associated-control */
/* eslint-disable react/react-in-jsx-scope */
/* eslint-disable react/prop-types */
import './App.css';

// eslint-disable-next-line import/prefer-default-export
export function Comment({
  deleteComment, id, updateComment, text, rating, updateRating,
}) {
  return (
    <div>
      <form className="comment" action="/comment" method="POST">
        <label htmlFor="comment">Comment</label>
        <input minLength="3" maxLength="100" type="text" name="comment" onChange={(e) => updateComment(id, e.target.value, rating)} value={text} />

        <label htmlFor="rating">Rating</label>

        <select name="rating" onChange={(e) => updateRating(id, text, e.target.value)} value={rating}>
          {[...Array(10)].map((_x, i) => <option value={i + 1}>{i + 1}</option>)}
        </select>
      </form>
      <button onClick={() => deleteComment(id)}>Delete Comment</button>

    </div>
  );
}
