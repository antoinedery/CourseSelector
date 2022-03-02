import { Component, ElementRef, ViewChild } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { User } from '@app/classes/user';
import { ClientSocketService } from '@app/services/client-socket.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss'],
})
export class HomePageComponent {
  @ViewChild('usernameInput') usernameInput!: ElementRef;
  @ViewChild('passwordInput') passwordInput!: ElementRef;
  @ViewChild('dobInput') dobInput!: ElementRef;
  @ViewChild('emailInput') emailInput!: ElementRef;
  @ViewChild('passwordVisibility') passwordVisibility!: ElementRef;
  @ViewChild('coursesButtonContainer') coursesButtonContainer!: ElementRef;
  @ViewChild('courseSearchInput') courseSearchInput!: ElementRef;
  chosenCourses: string[] = [];
  sortedSuggestions: string[] = [];
  courseCode: string = '';
  date: Date = new Date();
  isPasswordVisible: boolean = false;
  isCoursesVisible: boolean = false;
  coursesHeight: number = 50;

  constructor(
    public clientSocketService: ClientSocketService,
    private snackBar: MatSnackBar
  ) {
    this.getList();
    this.sortedSuggestions = this.clientSocketService.courses;
  }

  submit(): void {
    const user: User = {
      username: '',
      password: '',
      dob: '',
      email: '',
      courses: '',
    };
    user.username = this.usernameInput.nativeElement.value;
    user.password = this.passwordInput.nativeElement.value;
    user.dob = this.dobInput.nativeElement.value.replaceAll('-', '');
    user.email = this.emailInput.nativeElement.value;
    user.courses = this.chosenCourses.toString();
    if (
      user.username.length < 0 ||
      user.password.length < 0 ||
      user.dob.length < 0 ||
      user.email.length < 0 ||
      user.dob.length < 0 ||
      user.courses.length < 0
    )
      return;

    this.clientSocketService.sendDataToServer(user);
  }

  getList(): void {
    this.clientSocketService.getList();
  }

  togglePasswordVisibility(): void {
    if (this.isPasswordVisible) {
      this.passwordVisibility.nativeElement.classList.remove('fa-eye');
      this.passwordVisibility.nativeElement.classList.add('fa-eye-slash');
      this.passwordInput.nativeElement.setAttribute('type', 'password');
    } else {
      this.passwordVisibility.nativeElement.classList.remove('fa-eye-slash');
      this.passwordVisibility.nativeElement.classList.add('fa-eye');
      this.passwordInput.nativeElement.setAttribute('type', 'text');
    }
    this.isPasswordVisible = !this.isPasswordVisible;
  }

  toggleCoursesVisibility(event: MouseEvent): void {
    const target = (event.target || event.currentTarget) as Element;
    if (target.id === 'course-name' || target.id === 'remove-course-btn')
      return;

    if (this.isCoursesVisible) {
      this.coursesButtonContainer.nativeElement.style.borderBottom =
        '1px solid black';
      this.coursesButtonContainer.nativeElement.style.borderBottomLeftRadius =
        '3px';
      this.coursesButtonContainer.nativeElement.style.borderBottomRightRadius =
        '3px';
    } else {
      this.coursesButtonContainer.nativeElement.style.borderBottom = '0px';
      this.coursesButtonContainer.nativeElement.style.borderBottomLeftRadius =
        '0px';
      this.coursesButtonContainer.nativeElement.style.borderBottomRightRadius =
        '0px';
    }

    setTimeout(() => {
      if (this.courseSearchInput) this.courseSearchInput.nativeElement.focus();
    }, 100);

    this.isCoursesVisible = !this.isCoursesVisible;
    if (this.courseSearchInput) {
      this.courseCode = '';
      this.sortCoursesList('');
    }
  }

  removeCourse(index: number): void {
    this.chosenCourses.splice(index, 1);
    this.adjustHeight();
  }

  selectCourse(index: number): void {
    const courseCode = this.sortedSuggestions[index].split(' ')[0];
    if (this.chosenCourses.includes(courseCode)) {
      this.snackBar.open(courseCode + ' est déjà sélectionné.', 'OK', {
        duration: 3000,
        verticalPosition: 'bottom',
        panelClass: ['snack-bar'],
      });
      return;
    } else if (this.chosenCourses.length >= 8) {
      this.snackBar.open('Nombre de cours maximal atteint.', 'OK', {
        duration: 3000,
        verticalPosition: 'bottom',
        panelClass: ['snack-bar'],
      });
      return;
    }
    this.chosenCourses.push(this.sortedSuggestions[index].split(' ')[0]);
    this.sortCoursesList('');
    this.adjustHeight();
  }

  adjustHeight(): void {
    const rows = Math.ceil(this.chosenCourses.length / 4);
    this.coursesHeight = 50 * rows + (rows - 1) * 7.5;
  }

  sortCoursesList(courseCode: string): void {
    this.courseSearchInput.nativeElement.value = courseCode;
    this.sortedSuggestions = [];
    if (courseCode.length === 0)
      this.sortedSuggestions = this.clientSocketService.courses;
    else {
      for (const course of this.clientSocketService.courses) {
        if (course.startsWith(courseCode.toUpperCase()))
          this.sortedSuggestions.push(course);
      }
    }
  }
}
