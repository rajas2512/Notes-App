function deleteNote(noteId) { //It is going to take noteID that we passed and
    fetch("/delete-note", { //going to send POST reqst to the delete note end point w
      method: "POST",       
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/"; 
      // ANd then gets response from the delete note end point its going to reload the window with GET reqst
      // it redirects us to homepage 
    });
  }