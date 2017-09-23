import React, { Component } from 'react';
//Material UI Imports
import {Timeline} from 'react-twitter-widgets'

class TwitterTimeline extends Component {
  render() {
    return (
      <div>
        <Timeline
          dataSource={{
            sourceType: 'url',
            url: 'https://twitter.com/hashtag/UFCJapan?src=tren'
          }}
          options={{
            username: 'TwitterDev',
            height: '400'
          }}
          onLoad={() => console.log('Timeline is loaded!')}
        />
      </div>
    );
  }
}

export default TwitterTimeline;
