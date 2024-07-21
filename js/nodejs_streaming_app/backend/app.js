const express = require('express');
const fs = require('fs');
const cors = require('cors');
const path = require('path');
const app = express();


app.use(cors())

const Videos = require('./routes/Video')
app.use('/videos', Videos)

app.listen(5000, () => {
    console.log('Listening on port 5000!')
    console.log(__dirname)
});


// info
// https://gist.github.com/thanhtoan1196/36ebe18c5c14a13b7606bb328fa2e5e4
// https://stackoverflow.com/questions/55460359/streaming-an-mkv-file-while-processing-with-ffmpeg
// https://www.reddit.com/r/ffmpeg/comments/nh2zqj/stream_mkv_or_live_transcode_on_the_fly_nodejs/
// https://spectrum.chat/node/general/has-anyone-tried-real-time-video-transcoding-with-node-js~6e37fbe1-0330-4f86-b1f3-74c4d973a4c0
// https://betterprogramming.pub/video-stream-with-node-js-and-html5-320b3191a6b6
// https://nodejs.org/en/docs/guides/backpressuring-in-streams/
// https://www.smashingmagazine.com/2021/04/building-video-streaming-app-nuxtjs-node-express/
// https://github.com/smashingmagazine/Nuxt-Node-video-streaming/tree/main/backend
