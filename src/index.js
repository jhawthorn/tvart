import { h } from 'preact';
import { useState, useEffect } from 'preact/hooks';
import './style';

function Artwork(props) {
  const {artwork, onSelect, onDelete} = props;

  let classNames = ["artwork"];
  if (artwork.selected) {
    classNames.push("artwork-selected");
  }

  return (
    <div className={classNames}>
      <div className="artwork-image">
        <div className="artwork-selected-icon">✅</div>
        <img src={`api/preview/${props.artwork.content_id}.jpg`} />
      </div>
      <div className="artwork-info">
        date: { artwork.image_date }<br/>
        matte: { artwork.matte_id }<br/>
        {/*portrait matte: { artwork.portrait_matte_id }<br/>*/}
        size: { artwork.width } x { artwork.height }<br/>
      </div>
      <div className="artwork-actions">
        <button onClick={onSelect}>select</button>
        <button onClick={onDelete}>delete</button>
      </div>
    </div>
  );
}

function ArtworkUpload(props) {
  return (
    <div class="artwork-upload">
      <form method="post" action="/api/upload" enctype="multipart/form-data">
        <input type="file" name="image" />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default function App() {
  const [artworks, setArtworks] = useState([]);

  const fetchData = () => {
    fetch("/api/available.json")
      .then(response => {
        return response.json()
      })
      .then(data => {
        console.log("setting")
        setArtworks(data)
      })
  };

  useEffect(() => {
    fetchData()
  }, []);

  const selectArtwork = (artwork) => {
    fetch(`/api/select/${artwork.content_id}`, {
      method: 'POST',
    }).then(() => fetchData())
  };

  const deleteArtwork = (artwork) => {
    if (confirm("are you sure you want to delete this artwork?")) {
      fetch(`/api/delete/${artwork.content_id}`, {
        method: 'POST',
      }).then(() => fetchData())
    }
  };

  return (
    <div>

    <div className="header">
      <button onClick={fetchData}>↻</button>
    </div>

    <h1>TV ART!</h1>

    <ArtworkUpload />

    <div className="artwork-list">
        {artworks.map((artwork, i) =>
          <Artwork
          artwork={artwork}
          onSelect={() => selectArtwork(artwork)}
          onDelete={() => deleteArtwork(artwork)}
          key={i}
          />)}
    </div>

    </div>
  );
}
