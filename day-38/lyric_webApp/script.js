const form = document.querySelector("#lyrics-form");
const artistInput = document.querySelector("#artist");
const titleInput = document.querySelector("#title");
const searchButton = document.querySelector("#search-button");
const clearButton = document.querySelector("#clear-button");
const zoomOutButton = document.querySelector("#zoom-out");
const zoomInButton = document.querySelector("#zoom-in");
const lyricsDisplay = document.querySelector("#lyrics-display");
const themeOptions = document.querySelectorAll('input[name="theme"]');

const MIN_FONT_SIZE = 8;
const MAX_FONT_SIZE = 40;
const FONT_STEP = 2;
let currentFontSize = 16;

function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  const selectedOption = document.querySelector(
    `input[name="theme"][value="${theme}"]`,
  );
  if (selectedOption) selectedOption.checked = true;
  localStorage.setItem("lyrify-theme", theme);
}

function setFontSize(size) {
  currentFontSize = Math.min(MAX_FONT_SIZE, Math.max(MIN_FONT_SIZE, size));
  lyricsDisplay.style.fontSize = `${currentFontSize}px`;
  zoomOutButton.disabled = currentFontSize === MIN_FONT_SIZE;
  zoomInButton.disabled = currentFontSize === MAX_FONT_SIZE;
}

function showMessage(message) {
  lyricsDisplay.textContent = message;
  lyricsDisplay.scrollTop = 0;
}

function toDisplayName(value) {
  return value.replace(/\b\w/g, (character) => character.toUpperCase());
}

async function fetchLyrics(event) {
  event.preventDefault();

  const artistName = artistInput.value.trim();
  const titleName = titleInput.value.trim();

  // Match the desktop app: clear the song title after each search.
  titleInput.value = "";
  showMessage("");

  if (!artistName || !titleName) {
    showMessage("Please enter both an artist name and a song title.");
    return;
  }

  searchButton.disabled = true;
  searchButton.textContent = "Searching...";
  showMessage("Searching for lyrics...");

  const endpoint = `https://api.lyrics.ovh/v1/${encodeURIComponent(artistName)}/${encodeURIComponent(titleName)}`;

  try {
    const response = await fetch(endpoint, {
      headers: { Accept: "application/json" },
    });
    const data = await response.json();

    if (response.ok && data.lyrics) {
      const heading = `${toDisplayName(titleName)} by ${toDisplayName(artistName)}`;
      showMessage(
        `${heading}\n----------------------------------------------\n${data.lyrics}`,
      );
    } else {
      showMessage(
        `Sorry, no lyrics found for '${toDisplayName(titleName)}' by ${toDisplayName(artistName)}.`,
      );
    }
  } catch (error) {
    showMessage(
      `Network error: Could not connect to the API.\n\nDetails: ${error.message}`,
    );
  } finally {
    searchButton.disabled = false;
    searchButton.textContent = "Get Lyrics";
  }
}

function clearFields() {
  artistInput.value = "";
  titleInput.value = "";
  showMessage("");
  artistInput.focus();
}

form.addEventListener("submit", fetchLyrics);
clearButton.addEventListener("click", clearFields);
zoomOutButton.addEventListener("click", () =>
  setFontSize(currentFontSize - FONT_STEP),
);
zoomInButton.addEventListener("click", () =>
  setFontSize(currentFontSize + FONT_STEP),
);
themeOptions.forEach((option) => {
  option.addEventListener("change", () => applyTheme(option.value));
});

document.addEventListener("keydown", (event) => {
  if (!event.ctrlKey && !event.metaKey) return;

  if (event.key === "+" || event.key === "=") {
    event.preventDefault();
    setFontSize(currentFontSize + FONT_STEP);
  } else if (event.key === "-") {
    event.preventDefault();
    setFontSize(currentFontSize - FONT_STEP);
  }
});

const savedTheme = localStorage.getItem("lyrify-theme");
const initialTheme = ["dark", "light", "earthy"].includes(savedTheme)
  ? savedTheme
  : "dark";
applyTheme(initialTheme);
setFontSize(currentFontSize);
