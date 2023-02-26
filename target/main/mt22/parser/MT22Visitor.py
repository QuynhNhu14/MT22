# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MT22Parser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortDeclaration.
    def visitShortDeclaration(self, ctx:MT22Parser.ShortDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#longDeclaration.
    def visitLongDeclaration(self, ctx:MT22Parser.LongDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initializer.
    def visitInitializer(self, ctx:MT22Parser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifiers.
    def visitIdentifiers(self, ctx:MT22Parser.IdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typeName.
    def visitTypeName(self, ctx:MT22Parser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MT22Parser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionPrototype.
    def visitFunctionPrototype(self, ctx:MT22Parser.FunctionPrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameters.
    def visitParameters(self, ctx:MT22Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatement.
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockItem.
    def visitBlockItem(self, ctx:MT22Parser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MT22Parser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStatement.
    def visitIfStatement(self, ctx:MT22Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStatement.
    def visitForStatement(self, ctx:MT22Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStatement.
    def visitWhileStatement(self, ctx:MT22Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_whileStatement.
    def visitDo_whileStatement(self, ctx:MT22Parser.Do_whileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStatement.
    def visitBreakStatement(self, ctx:MT22Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStatement.
    def visitContinueStatement(self, ctx:MT22Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStatement.
    def visitReturnStatement(self, ctx:MT22Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStatement.
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressions.
    def visitExpressions(self, ctx:MT22Parser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringExpression.
    def visitStringExpression(self, ctx:MT22Parser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalExpression.
    def visitRelationalExpression(self, ctx:MT22Parser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalExpression.
    def visitLogicalExpression(self, ctx:MT22Parser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MT22Parser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MT22Parser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unaryExpression.
    def visitUnaryExpression(self, ctx:MT22Parser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#signExpression.
    def visitSignExpression(self, ctx:MT22Parser.SignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#postfixExpression.
    def visitPostfixExpression(self, ctx:MT22Parser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primaryExpression.
    def visitPrimaryExpression(self, ctx:MT22Parser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionCall.
    def visitFunctionCall(self, ctx:MT22Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)



del MT22Parser