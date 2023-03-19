# Description

Currently, there is no way to delete completed scan files in Scan8, which is problematic for users who want to remove unnecessary scan files from their system. However, I have implemented a delete button that can be used to delete completed scans. When pressed, the button will remove the completed scan files immediately.



Fixes # (issue)

The delete button has been added to the "Completed Scans" section of the Scan8 tool, and is easily accessible to users. It is labeled with a trash can icon and has been styled to match the existing Scan8 user interface. The delete button works as expected, and removes the completed scan files without causing any unintended consequences.

## Type of change

Please delete options that are not relevant.


- [ ] New feature (non-breaking change which adds functionality)


# Testing

The application comes with a test suite to help users ensure correct installation and help developers verify any updates. 

The following tests should return **ok** status upon running the unit-test command `python3 app.py -v` from the `/Testing` directory.

- [ ] `testResultsJSON`
- [ ] `testResults`
- [ ] `testUploads`
- [ ] `testResultsDirectoryPresent`
- [ ] `testUploadsDirectoryPresent`
# Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
