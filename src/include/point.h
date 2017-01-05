//
// point.h
//
// phase space point
//

#ifndef POINT_H
#define POINT_H

#include <iostream>
#include <iomanip>

class Point
{
    public:
        Point() : x_ { 0.0 }, y_ { 0.0 } {}
        Point(double const & x, double const & y) : x_ { x }, y_ { y } {}

        double const & x() const { return x_; }
        double const & y() const { return y_; }   

    private:
        double x_;
        double y_;
};


//
//class Point
//{
//    public:
//        Point() : x_(0.0), y_(0.0) {}
//        Point(double x, double y) : x_(x), y_(y) {}
//
//        double const & x() const { return x_; }
//        double const & y() const { return y_; }   
//
//        // friendly input operator
//        friend std::istream & operator>>(std::istream & is, Point & point)
//        {
//            is >> point.x_ >> point.y_;
//            return is;
//        }
//
//        // friendly output operator
//        friend std::ostream & operator<<(std::ostream & os, Point const & point)
//        {
//            os << std::fixed;
//            os << "_X_";
//            os << std::setw(5) << std::setfill('_') << std::setprecision(2) << point.x_;
//            os << "_Y_";
//            os << std::setw(5) << std::setfill('_') << std::setprecision(2) << point.y_;
//            return os;
//        }
//
//    private:
//        double x_;
//        double y_;
//};
//
#endif
