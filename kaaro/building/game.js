function initProfile() {
    localforage.getItem('profile_name', (e) => {
        console.log(e);
    });
}

initProfile();