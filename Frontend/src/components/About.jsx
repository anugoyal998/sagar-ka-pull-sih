import React from "react";
import "../assets/css/About.css";
import {
  Animator,
  ScrollContainer,
  ScrollPage,
  batch,
  Fade,
  Move,
  MoveOut,
  Sticky,
} from "react-scroll-motion";

function About() {
  const FadeUp = batch(Fade(), Move(), Sticky());
  return (
    <div className="about_bg">
      <ScrollContainer>
        <ScrollPage>
          <Animator
            animation={batch(Fade(), Sticky(), MoveOut(0, -200))}
          ></Animator>
        </ScrollPage>
        <ScrollPage></ScrollPage>
        <ScrollPage>
          <Animator animation={FadeUp}>
            <span style={{ fontSize: "60px" }}>About</span>
          </Animator>
        </ScrollPage>

        <ScrollPage>
          <Animator animation={batch(Fade(), Sticky())}>
            <span style={{ fontSize: "40px" }}>
              {" "}
              Revolutionizing Safety and Efficiency with Macine Learning"
            </span>
            <br />
            <span style={{ fontSize: "20px" }}>
              Our comprehensive surveillance solution incorporates a range of
              cutting-edge features, including crowd management, weapon
              detection, fire and smoke detection, garbage detection, and facial
              recognition. Utilizing advanced ML algorithms, our system ensures
              public safety through real-time crowd monitoring and early threat
              detection. It swiftly identifies concealed weapons and triggers
              alerts to authorities, enhances fire safety with instant fire and
              smoke detection, maintains clean environments by flagging
              littering, and prioritizes privacy by blurring faces during
              routine crowd counting, only revealing faces when a security
              threat is detected. This holistic approach enhances security and
              safety while respecting individual privacy and fostering civic
              responsibility.
            </span>
          </Animator>
        </ScrollPage>
      </ScrollContainer>
    </div>
  );
}

export default About;
