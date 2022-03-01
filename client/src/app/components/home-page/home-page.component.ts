import { Component, ElementRef, ViewChild } from '@angular/core';
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
  @ViewChild('coursesInput') coursesInput!: ElementRef;
  @ViewChild('passwordVisibility') passwordVisibility!: ElementRef;
  @ViewChild('coursesButtonContainer') coursesButtonContainer!: ElementRef;
  courses: string[] = ['LOG2410', 'LOG2420'];
  date: Date = new Date();
  isPasswordVisible: boolean = false;
  isCoursesVisible: boolean = false;
  coursesHeight: number = 35;

  constructor(public clientSocketService: ClientSocketService) {
    this.getList();
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
    user.courses = this.coursesInput.nativeElement.value;

    // if (
    //   user.username.length < 0 ||
    //   user.password.length < 0 ||
    //   user.dob.length < 0 ||
    //   user.email.length < 0 ||
    //   user.dob.length < 0 ||
    //   user.courses.length < 0
    // )
    //   return;

    // this.clientSocketService.sendDataToServer(user);
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
    this.isCoursesVisible = !this.isCoursesVisible;
  }

  removeCourse(index: number): void {
    this.courses.splice(index, 1);
    this.adjustHeight();
  }

  selectCourse(index: number): void {
    const courseCode = this.clientSocketService.courses[index].split(' ')[0];
    if (this.courses.includes(courseCode)) return;
    this.courses.push(this.clientSocketService.courses[index].split(' ')[0]);
    this.adjustHeight();
  }

  adjustHeight():void{
    const rows = Math.ceil(this.courses.length / 3);
    this.coursesHeight = 35 * rows + ((rows - 1) * 5);
  }
}
