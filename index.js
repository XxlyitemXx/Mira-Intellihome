const simpleGit = require('simple-git');
const fs = require('fs');
const path = require('path');

const git = simpleGit();

async function makeCommit() {
    // Update a file
    const filePath = path.join(__dirname, 'daily_update.txt');
    fs.appendFileSync(filePath, `Update on ${new Date()}\n`);

    try {
        // Fetch repository URL
        const remote = await git.remote(['-v']);
        console.log('Repository URL:', remote);

        // Git operations
        await git.add('./*');
        await git.commit('Daily update');
        await git.push('origin', 'main');
    } catch (error) {
        console.error('Failed to commit and push changes:', error);
    }
}
makeCommit();