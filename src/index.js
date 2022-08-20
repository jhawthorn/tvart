import { h } from 'preact';
import { useState, useEffect } from 'preact/hooks';
import './style';

function Artwork(props) {
  const artwork = props.artwork;

  const selectArtwork = () => {
    fetch(`/api/select/${artwork.content_id}`, {
      method: 'POST',
    })
  };

  return (
    <div onClick={selectArtwork}>
      <img src={`api/preview/${props.artwork.content_id}.jpg`} />
    </div>
  );
}
export default function App() {
  const [artworks, setArtworks] = useState([])

  const fetchData = () => {
    fetch("/api/available.json")
      .then(response => {
        return response.json()
      })
      .then(data => {
        setArtworks(data)
      })
  }
  useEffect(() => {
    fetchData()
  }, [])

  return (
    <div>
    <h1>TV ART!</h1>
    <div class="artwork-list">
        {artworks.map((object, i) => <Artwork artwork={object} key={i} />)}
    </div>
    </div>
  );
}
