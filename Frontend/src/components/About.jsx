import React from "react";
import "../assets/css/About.css";
import {
  Animator,
  ScrollContainer,
  ScrollPage,
  batch,
  Fade,
  FadeIn,
  FadeOut,
  Move,
  MoveIn,
  MoveOut,
  Sticky,
  StickyIn,
  StickyOut,
  Zoom,
  ZoomIn,
  ZoomOut,
} from "react-scroll-motion";

function About() {
  const ZoomInScrollOut = batch(StickyIn(), FadeIn(), ZoomIn());
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
            <span style={{ fontSize: "40px" }}>About Us</span>
          </Animator>
        </ScrollPage>

        <ScrollPage>
          <Animator animation={batch(Fade(), Sticky())}>
            <span style={{ fontSize: "40px" }}>Crowd Management System</span>
            <br />
            <span style={{ fontSize: "30px" }}>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum
              similique nihil necessitatibus enim! Commodi vel dolor excepturi
              non, nemo obcaecati accusamus est? Voluptate sit alias commodi.
              Esse qui deserunt minus.
            </span>
          </Animator>
        </ScrollPage>
      </ScrollContainer>
    </div>
  );
}

export default About;
