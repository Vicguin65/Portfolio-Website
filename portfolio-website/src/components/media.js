const MEDIA_BASE = "https://whoistylerdu.com/media";
const asset = (slug, filename) => `${MEDIA_BASE}/${slug}/${filename}`;

const media = [
  {
    slug: "fyre-robotics-feature",
    title:
      "New Robotics Center for Students Opens in Old Southside School Building",
    publication: "This Is Reno",
    date: new Date(2021, 7, 6),
    description:
      "This Is Reno covered the opening of the FYRE Robotics center, a new space for students in the Southside neighborhood of Reno. The article features the mission of the program and the students involved in getting it off the ground.",
    tags: ["Robotics", "Community"],
    links: [
      {
        label: "Read on This Is Reno",
        url: "https://thisisreno.com/2021/08/new-robotics-center-for-students-opens-in-old-southside-school-building/",
      },
    ],
    images: [
      {
        src: asset("fyre-robotics-feature", "TylerRobotics.png"),
        alt: "Tyler at the FYRE Robotics center opening",
        caption: "",
      },
    ],
    videos: [],
  },
  {
    slug: "national-cyber-scholar-2021",
    title: "10 Nevada High School Students Named National Cyber Scholars",
    publication: "Nevada Department of Education",
    date: new Date(2021, 4, 27),
    description:
      "The Nevada Department of Education recognized 10 high school students, including Tyler Du, as National Cyber Scholars — a distinction awarded to top performers in the National Cyber Scholarship Foundation's CyberStart America program.",
    tags: ["Cybersecurity", "Award"],
    links: [
      {
        label: "Read the press release",
        url: "https://doe.nv.gov/news-media/2021-press-releases/10-nevada-high-school-students-named-national-cyber-scholars",
      },
    ],
    images: [],
    videos: [],
  },
  {
    slug: "ai-camp-internship-2021",
    title: "Our Experience With a Life-Changing Internship",
    publication: "Medium",
    date: new Date(2021, 10, 29),
    description:
      "A reflection written at the conclusion of the AI Camp internship, covering the projects built, skills gained, and the broader impact the program had on the cohort's understanding of machine learning and professional development.",
    tags: ["AI", "Internship"],
    links: [
      {
        label: "Read on Medium",
        url: "https://medium.com/@watermelonbread/our-experience-with-a-life-changing-internship-fd79eba22983",
      },
    ],
    images: [
      {
        src: asset("ai-camp-internship-feature", "ZoomAICamp.jpg"),
        alt: "Zoom meeting for AI Camp Internship",
        caption: "",
      },
    ],
    videos: [],
  },
];

export { media, asset };
