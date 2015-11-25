const LivePlaylist = React.createClass({
  getInitialState() { return { cuePoints: [] } },

  componentDidMount() {
    const ws = new WebSocket(this.props.server);
    this.setState({ ws });

    ws.onopen = () => this._send({ command: 'list_cue_points' });
    ws.onmessage = (msg) => {
      this.setState({ cuePoints: JSON.parse(msg.data).response });
    };
  },

  _send(msg) {
    this.state.ws.send(JSON.stringify(msg));
  },

  render() {
    return <div>
      {
        this.state.cuePoints.map((cuePoint) =>
          <div className="cue-point"
            key={cuePoint.name+cuePoint.position}
            onClick={() => this._send({ command: 'play_cue_point', data: cuePoint })}>
            {cuePoint.name}
          </div>
        )
      }
    </div>
  }
});

ReactDOM.render(
  <LivePlaylist server="ws://localhost:55455"/>,
  document.getElementById('root')
);
