document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("tutorialModal");
    const closeButton = modal.querySelector(".close");
    const steps = modal.querySelectorAll(".step");
    let currentStep = 0;
  
    // Show the modal
    modal.style.display = "block";
  
    // Function to show the current step
    function showStep(stepIndex) {
        steps.forEach((step, index) => {
            if (index === stepIndex) {
                step.classList.add("active");
            } else {
                step.classList.remove("active");
            }
        });
    }
  
    // Function to go to the next step
    function nextStep() {
        currentStep++;
        if (currentStep < steps.length) {
            showStep(currentStep);
        } else {
            modal.style.display = "none";
        }
    }
  
    // Function to go to the previous step
    function prevStep() {
        currentStep--;
        if (currentStep >= 0) {
            showStep(currentStep);
        }
    }
  
    // Function to skip to the last step
    function skipToLastStep() {
        currentStep = steps.length - 1;
        showStep(currentStep);
    }
  
    // Close the modal when clicking on the close button
    closeButton.addEventListener("click", function() {
        modal.style.display = "none";
    });
  
    // Close the modal when clicking outside the modal content
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
  
    // Event listeners for next, previous, and skip buttons
    const nextButtons = modal.querySelectorAll(".next-button");
    nextButtons.forEach(button => {
        button.addEventListener("click", nextStep);
    });
  
    const prevButtons = modal.querySelectorAll(".prev-button");
    prevButtons.forEach(button => {
        button.addEventListener("click", prevStep);
    });
  
    const skipButton = modal.querySelector(".skip-button"); // Define the skipButton variable
  skipButton.addEventListener("click", function() {
      modal.style.display = "none"; // Close the modal completely
  }); // Add event listener for the skip button
  });
  
 
  const checkboxes = document.querySelectorAll('.completed-checkbox');

  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
      updateProgress();
      updateMainCourseCompletion(this.closest('.course')); // Pass the parent course element to updateMainCourseCompletion
    });
  });
  
  function updateProgress() {
    const totalCourses = document.querySelectorAll('.sub-course').length;
    const completedCourses = document.querySelectorAll('.completed-checkbox:checked').length;
    const progressPercentage = Math.min(Math.round((completedCourses / totalCourses) * 100), 100);

    const progressText = document.querySelector('.progress-text');
    progressText.textContent = progressPercentage + '%';

    const progressCircle = document.querySelector('.progress-circle');
    const circleLength = 2 * Math.PI * progressCircle.getAttribute('r'); // Circumference of the circle
    const strokeDashArray = circleLength;
    const strokeDashOffset = circleLength - (circleLength * progressPercentage) / 100;
    progressCircle.style.strokeDasharray = strokeDashArray;
    progressCircle.style.strokeDashoffset = strokeDashOffset;

    progressCircle.style.transition = 'stroke-dashoffset 0.3s ease'; // Add transition effect
  }

  function updateMainCourseCompletion(course) {
    const subCourses = course.querySelectorAll('.sub-course');
    const totalSubCourses = subCourses.length;
    let completedSubCourses = 0;

    subCourses.forEach(subCourse => {
      const checkbox = subCourse.querySelector('.completed-checkbox');
      if (checkbox.checked) {
        completedSubCourses++;
      }
    });

    const mainCourseProgressPercentage = Math.min(Math.round((completedSubCourses / totalSubCourses) * 100), 100);

    const progressText = course.querySelector('.progress-text');
    progressText.textContent = mainCourseProgressPercentage + '%';

    const progressCircle = course.querySelector('.progress-circle');
    const circleLength = 2 * Math.PI * progressCircle.getAttribute('r'); // Circumference of the circle
    const strokeDashOffset = circleLength - (circleLength * mainCourseProgressPercentage) / 100;
    progressCircle.style.strokeDashoffset = strokeDashOffset;

    if (completedSubCourses === totalSubCourses) {
      course.classList.add('completed');
    } else {
      course.classList.remove('completed');
    }
  }
  const saveButton = document.querySelector('.save-progress-button');
saveButton.addEventListener('click', function() {
  // Here you can implement functionality to save the completion track, such as using localStorage or sending data to a server
  alert('Progress saved successfully!');
});
// JavaScript to display the tutorial modal

document.addEventListener("DOMContentLoaded", function() {
  const modal = document.getElementById("tutorialModal");
  const closeButton = modal.querySelector(".close");
  const steps = modal.querySelectorAll(".step");
  let currentStep = 0;

  // Show the modal
  modal.style.display = "block";

  // Function to show the current step
  function showStep(stepIndex) {
      steps.forEach((step, index) => {
          if (index === stepIndex) {
              step.classList.add("active");
          } else {
              step.classList.remove("active");
          }
      });
  }

  // Function to go to the next step
  function nextStep() {
      currentStep++;
      if (currentStep < steps.length) {
          showStep(currentStep);
      } else {
          modal.style.display = "none";
      }
  }

  // Function to go to the previous step
  function prevStep() {
      currentStep--;
      if (currentStep >= 0) {
          showStep(currentStep);
      }
  }

  // Function to skip to the last step
  function skipToLastStep() {
      currentStep = steps.length - 1;
      showStep(currentStep);
  }

  // Close the modal when clicking on the close button
  closeButton.addEventListener("click", function() {
      modal.style.display = "none";
  });

  // Close the modal when clicking outside the modal content
  window.addEventListener("click", function(event) {
      if (event.target === modal) {
          modal.style.display = "none";
      }
  });

  // Event listeners for next, previous, and skip buttons
  const nextButtons = modal.querySelectorAll(".next-button");
  nextButtons.forEach(button => {
      button.addEventListener("click", nextStep);
  });

  const prevButtons = modal.querySelectorAll(".prev-button");
  prevButtons.forEach(button => {
      button.addEventListener("click", prevStep);
  });

});

